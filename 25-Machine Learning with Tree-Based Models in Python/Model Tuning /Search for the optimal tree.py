'''In this exercise, you'll perform grid search using 5-fold cross validation to find dt's optimal hyperparameters. Note that because grid search is an exhaustive process, it may take a lot time to train the model. Here you'll only be instantiating the GridSearchCV object without fitting it to the training set. As discussed in the video, you can train such an object similar to any scikit-learn estimator by using the .fit() method:

grid_object.fit(X_train, y_train) An untuned classification tree dt as well as the dictionary params_dt that you defined in the previous exercise are available in your workspace.'''

df = indian_liver_patient.rename(columns={'Dataset':'Liver_disease'})
df = df.dropna()

X = df[['Age', 'Total_Bilirubin',
        'Direct_Bilirubin',
        'Alkaline_Phosphotase',
        'Alamine_Aminotransferase', 'Aspartate_Aminotransferase',
       'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio', 'Gender']]
y = df['Liver_disease']-1

LabelEncoder = sklearn.preprocessing.LabelEncoder()
X['Is_male'] = LabelEncoder.fit_transform(X['Gender'])
X = X.drop(columns='Gender')

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)
print(X_train.shape,y_train.shape)

# Define params_dt
params_dt = {'max_depth':[2,3,4], 'min_samples_leaf':[0.12,0.14,0.16,0.18]}

# Import GridSearchCV
from sklearn.model_selection import GridSearchCV

dt = sklearn.tree.DecisionTreeClassifier()

# Instantiate grid_dt
grid_dt = GridSearchCV(estimator=dt,
                       param_grid=params_dt,
                       scoring='roc_auc',
                       cv=5,
                       n_jobs=-1)
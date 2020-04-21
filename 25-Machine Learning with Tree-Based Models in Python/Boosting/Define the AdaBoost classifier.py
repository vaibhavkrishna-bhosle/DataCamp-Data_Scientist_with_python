'''In the following exercises you'll revisit the Indian Liver Patient dataset which was introduced in a previous chapter. Your task is to predict whether a patient suffers from a liver disease using 10 features including Albumin, age and gender. However, this time, you'll be training an AdaBoost ensemble to perform the classification task. In addition, given that this dataset is imbalanced, you'll be using the ROC AUC score as a metric instead of accuracy.

As a first step, you'll start by instantiating an AdaBoost classifier.'''

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

# Import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

# Import AdaBoostClassifier
from sklearn.ensemble import AdaBoostClassifier

# Instantiate dt
dt = DecisionTreeClassifier(max_depth=2, random_state=1)

# Instantiate ada
ada = AdaBoostClassifier(base_estimator=dt,
n_estimators=180, random_state=1)
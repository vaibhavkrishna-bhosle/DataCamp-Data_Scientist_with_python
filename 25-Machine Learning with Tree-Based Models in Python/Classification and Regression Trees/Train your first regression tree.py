'''In this exercise, you'll train a regression tree to predict the mpg (miles per gallon) consumption of cars in the auto-mpg dataset using all the six available features.

The dataset is processed for you and is split to 80% train and 20% test. The features matrix X_train and the array y_train are available in your workspace.

'''

df = auto

X = df[['displ', 'hp', 'weight', 'accel', 'size', 'origin']]
y = df['mpg']

OneHotEncoder = sklearn.preprocessing.OneHotEncoder()
OneHotEncodings = OneHotEncoder.fit_transform(df[['origin']]).toarray()
OneHotEncodings = pd.DataFrame(OneHotEncodings,
                               columns = ['origin_'+header for header in OneHotEncoder.categories_[0]])

X = X.drop(columns = 'origin').reset_index(drop=True)
X = pd.concat((X,OneHotEncodings),axis=1)


X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)
print(X_train.shape,y_train.shape)
(294, 8) (294,)

# Import DecisionTreeRegressor from sklearn.tree
from sklearn.tree import DecisionTreeRegressor

# Instantiate dt
dt = DecisionTreeRegressor(max_depth=8,
             min_samples_leaf=0.13,
            random_state=3)
lr = sklearn.linear_model.LinearRegression()

# Fit dt to the training set
dt.fit(X_train, y_train)
lr.fit(X_train,y_train)

'''In this exercise, you'll evaluate the 10-fold CV Root Mean Squared Error (RMSE) achieved by the regression tree dt that you instantiated in the previous exercise.

In addition to dt, the training data including X_train and y_train are available in your workspace. We also imported cross_val_score from sklearn.model_selection.

Note that since cross_val_score has only the option of evaluating the negative MSEs, its output should be multiplied by negative one to obtain the MSEs.'''

from sklearn.model_selection import cross_val_score

# Compute the array containing the 10-folds CV MSEs
MSE_CV_scores = - cross_val_score(dt, X_train, y_train, scoring = 'neg_mean_squared_error', cv=10,  n_jobs=-1)

# Compute the 10-folds CV RMSE
import numpy as np
RMSE_CV = np.sqrt(MSE_CV_scores.mean())

# Print RMSE_CV
print('CV RMSE: {:.2f}'.format(RMSE_CV))
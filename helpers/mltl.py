"""
mltl.py - a machine learning helper module
Auther: Theo Love
Date: 3/12/15
"""
import pandas as pd
import numpy as np


class Transformations(object):
    """
    A class of basic transformations
    """

    def __init__(self):
        pass

    def mean_at_zero(self, arr):
        """Return an array shifted so that the mean of the array is 0"""
        return np.array([i - np.mean(arr) for i in arr])

    def norm_to_min_zero(self, arr):
        """Return an array normalized to 0 and 1 (where 0 remains 0)"""
        return np.array([i / max(arr) for i in arr])
    
    def norm_to_absolute_min_zero(self, arr):
        """Return an array normalized to 0 and 1 (where min == 0)"""
        return np.array([(i - min(arr)) / (max(arr) - min(arr)) for i in arr])
    
    def norm_to_neg_pos(self, arr):
        """Returns an array normalized to -1 and 1 (where mean == 0)"""
        return np.array([(i - mean(arr)) / (max(arr) - mean(arr)) for i in arr])
    
    def norm_by_std(self, arr):
        """Returns an array standardized using mean and standard deviation (where mean = 0)"""
        return np.array([(i-mean(arr))/np.std(arr) for i in arr])

class Classification(object):
    """Generic classification model helpers"""
    from sklearn import tree, dummy, metrics, cross_validation

    def __init__(self):
        pass

    def basic_metrics(self, y_true, y_predict, print_out=False):
        """Returns basic classification metrics in a DataFrame for a y_true and y_predict, including
         * Accuracy
         * ROC AUC Score
         * Confusion matrix
        
        Optional argument to print results (default is False)
        """
        scores = []
        scores.append(['Accuracy', metrics.accuracy_score(y_true, y_predict)])
        scores.append(['ROC_AUC', metrics.roc_auc_score(y_true, y_predict)])
        scores.append(['Confusion_Matrix', metrics.confusion_matrix(y_true, y_predict)])
        if print_out:
            print "Accuracy: %0.4f" % scores[0][1]
            print "ROC AUC:  %0.4f" % scores[1][1]
            print "Confusion Matrix:"
            print scores[2][1]
        return scores

    def run_model(self, clf, X, y, test_size= 0.3, rstate=1234, print_out=False):
        """Performsa a train/test split on a sklearn classifier and returns it, printing metrics is optional
        Returns: a tuple (model, train_scores, test_scores)
                where model is the fitted model, and score is a DataFrame of basic metrics
        
        Arguments
        =========
        clf         : the sklearn classifier
        X           : matrix of independent variables
        y           : target variable (mus be a series)
        test_size   : test size as a percentage of the sample (default 0.30)
        rstate      : the seed for the train/test shuffler (default 1234)
        """
        
        # create the train/test split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=rstate)
        
        # fit the model
        clf.fit(X_train, y_train)
        if print_out:
            print model
            
        # get the metrics for the train and the test
        if print_out:
            print "\nTRAIN METRICS\n========"
        train_metrics = self.basic_metrics(y_train, model.predict(X_train), print_out)
        if print_out:
            print "\nTEST METRICS\n========"
        test_metrics = self.basic_metrics(y_test, model.predict(X_test), print_out)
        
        # return the fitted model and metrics for the train and test
        return (clf, train_metrics, test_metrics)

class DTreeClassification(Classification):
    """Decision tree classifier helper
    Inherits: Classification
    """

    def __init__(self):
        pass

    def cross_val_by_constraint(self, X, y, constraint="None", constraint_range=[2], splits=3, scoring='roc_auc', rstate=1234):
        """Returns cross validation average scores for varying constraints

        Arguments
        =========
        X                : matrix of independent variables
        y                : target variable (mus be a series)
        constraint       : 'None' (default), max_depth', 'min_samples_split', 'min_samples_leaf'
        constraint_range : the list of values on which to test the constraints (default [2])
        splits           : the number of folds on which to do train/test splits (default 3)
        scorign          : the name of a function from the sklearn.metrics (default 'roc_auc')
        rstate           : the seed for the random shuffle
        """
        all_scores = []
        all_constraints = []
        best_score = -1
        for i in constraint_range:
            # intialize the decision tree based on the constraint
            if constraint == 'max_depth':
                treereg = tree.DecisionTreeClassifier(max_depth=i, random_state=rstate)
            elif constraint == 'min_samples_split':
                treereg = tree.DecisionTreeClassifier(min_samples_split=i, random_state=rstate)
            elif constraint == 'min_samples_leaf':
                treereg = tree.DecisionTreeClassifier(min_samples_leaf=i, random_state=rstate)
            else:
                treereg = tree.DecisionTreeClassifier(random_state=rstate)

            # run the cross validation and save the mean score
            scores = cross_val_score(treereg, X, y, cv=splits, scoring=scoring)
            current_score = np.mean(scores)
            if current_score > best_score:
                best_score = current_score
                best_constraint = i

            # maintain the lists to return
            all_scores.append(current_score)
            all_constraints.append(i)

        return pd.DataFrame({constraint : all_constraints, 'scores': all_scores})
                
    def cross_val_by_depth(self, X, y, max_depth=2, splits=3, scoring='roc_auc', rstate=1234):
        """Calls cross_val_by_constraint for max depth from 2 to max_depth"""
        return self.cross_val_by_constraint(X=X,
                                           y=y,
                                           constraint='max_depth',
                                           constraint_range=range(2, max_depth),
                                           splits=splits,
                                           scoring=scoring,
                                           rstate=rstate)


class Linear(object):
    """A class of linear regression helpers"""
    import statsmodels.formula.api as smf
    from sklearn import feature_select as f_select
    from sklearn import linear_model as lm

    def __init__(self):
        pass

    def f_test(self, X, y, ci=0.9):
        """Return the signficant columns of X in a linear regression against y with confidence interval ci"""
        pvals = []
        fscores = []
        sig_cols = []

        for f in list(X.columns):
            pval = f_select.f_regression(X[f], y)
            if pval[1][0] < (1 - ci):
                sig_cols.append(f)
                fscores.append(pval[0][0])
                pvals.append(pval[1][0])

        return pd.DataFrame({'features' : sig_cols, 'p-values' : pvals, 'F score' : fscores })

    def smf_linear(self, X, y):
        """
        takes a pandas data frame of independent (X) variables and a dependent variable (y)
        returns the statsmodel linear model fit
        """
        return smf.ols(formula= ''.join(y.columns) + ' ~ ' + ' + '.join(X.columns),
                        data=y.join(X)).fit()


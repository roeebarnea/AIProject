import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def take_X_Y(WWC):
    Y = WWC['more_new_cases']
    X = WWC.drop(['Unnamed: 0.1.1', 'location', 'date', 'more_new_cases'], axis=1)
    return X, Y

def knn(WWC, k, tests):
    scores = []
    for i in range(tests):
        X, Y = take_X_Y(WWC)
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20)
        classifier = KNeighborsClassifier(n_neighbors=k)
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        #print(confusion_matrix(y_test, y_pred))
        #print(classification_report(y_test, y_pred))

        acc_knn = round(classifier.score(X_train, y_train) * 100, 2)
        scores.append(acc_knn)
        #print(acc_knn)

    print(scores)
    print(sum(scores) / len(scores))
    return sum(scores) / len(scores)

def knn_graph(WWC, neis, dataSetName):
    final_scores = [dataSetName]
    for i in range(1, neis):
        final_scores.append(knn(WWC, i, 10))
    return final_scores


if __name__ == '__main__':

    num_of_tests = 50

    col = ['DataSet']
    for i in range(1, num_of_tests):
        col += [str(i) + "_neighbours"]
    df_scores = pd.DataFrame(columns=col)


    # no_nulls_4_classes
    dataSetName = 'WWC_09_01_2021_no_nulls_4_classes'
    WWC_no_nulls_4_classes = pd.read_csv('WWC_09_01_2021_no_nulls_4_classes.csv')
    scores = knn_graph(WWC_no_nulls_4_classes, num_of_tests, dataSetName)

    df_scores.loc[len(df_scores)] = scores
    # ---------------------

    # no_nulls_8_classes
    dataSetName = 'WWC_09_01_2021_no_nulls_8_classes'
    WWC_no_nulls_8_classes = pd.read_csv('WWC_09_01_2021_no_nulls_8_classes.csv')
    scores = knn_graph(WWC_no_nulls_8_classes, num_of_tests, dataSetName)

    df_scores.loc[len(df_scores)] = scores
    # ---------------------

    # no_nulls_16_classes
    dataSetName = 'WWC_09_01_2021_no_nulls_16_classes'
    WWC_no_nulls_16_classes = pd.read_csv('WWC_09_01_2021_no_nulls_16_classes.csv')
    scores = knn_graph(WWC_no_nulls_16_classes, num_of_tests, dataSetName)

    df_scores.loc[len(df_scores)] = scores
    # ---------------------

    #------------------------------------------------------------------------------------------------------

    # no_nulls_4_classes
    dataSetName = 'WWC_09_01_2021_no_nulls_AVG_4_classes'
    WWC_no_nulls_avg_4_classes = pd.read_csv('WWC_09_01_2021_no_nulls_AVG_4_classes.csv')
    scores = knn_graph(WWC_no_nulls_avg_4_classes, num_of_tests, dataSetName)

    df_scores.loc[len(df_scores)] = scores
    # ---------------------

    # no_nulls_8_classes
    dataSetName = 'WWC_09_01_2021_no_nulls_AVG_8_classes'
    WWC_no_nulls_avg_8_classes = pd.read_csv('WWC_09_01_2021_no_nulls_AVG_8_classes.csv')
    scores = knn_graph(WWC_no_nulls_avg_8_classes, num_of_tests, dataSetName)

    df_scores.loc[len(df_scores)] = scores
    # ---------------------

    # no_nulls_16_classes
    dataSetName = 'WWC_09_01_2021_no_nulls_AVG_16_classes'
    WWC_no_nulls_avg_16_classes = pd.read_csv('WWC_09_01_2021_no_nulls_AVG_16_classes.csv')
    scores = knn_graph(WWC_no_nulls_avg_16_classes, num_of_tests, dataSetName)

    df_scores.loc[len(df_scores)] = scores
    # ---------------------


    df_scores.to_csv('WWC_09_01_2021_KNN_SCORES_ALL.csv')



    print("DONE")
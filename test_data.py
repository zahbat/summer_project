import pandas as pd
import numpy as np


########################################################################################################################
# This file prepares a random multivariate time series, if one wants to run some code without fluidity files #
########################################################################################################################

def build(split=3000):
    ds = pd.read_csv("eegtry.csv")

    ds = ds.drop("0", axis=1)
    
    ds = (ds - ds.mean().mean())/ds.std().std()

    X_ = []
    Y_1 = []
    Y_2 = []
    Y_3 = []

    for i in range(ds.shape[0]-3):
        if i%4==0:
            X_.append(i)
        elif i%4==1:
            Y_1.append(i)
        elif i%4==2:
            Y_2.append(i)
        else:
            Y_3.append(i)


    X_ds = ds.iloc[X_]
    Y1_ds = ds.iloc[Y_1]
    Y2_ds = ds.iloc[Y_2]
    Y3_ds = ds.iloc[Y_3]

    X = X_ds.to_numpy()
    Y1 = Y1_ds.to_numpy()
    Y2 = Y2_ds.to_numpy()
    Y3 = Y3_ds.to_numpy()


    Y = []

    for i in range(len(Y1)):
        Y.append([Y1[i], Y2[i], Y3[i]])
    
    Y = np.array(Y)

    X_train = X[:3000]
    X_test = X[3000:]

    Y_train = Y[:3000]
    Y_test = Y[3000:]
    
    return X_train, X_test, Y_train, Y_test


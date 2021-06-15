import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np


########################################################################################################################
# This file prepares simulation data, if one wants to run some code without fluidity working#
########################################################################################################################

def build(split=270, pca=False, pca_details=False, shuffle=False):
    """
    Returns a train/test splitted dataset ready to be converted to tensors for the learning part.
    Can also perform PCA on the data.
    """
    ds = pd.read_csv("out.csv", header=None)
    
    if pca:
        sc = StandardScaler()
        ds_ = sc.fit_transform(ds) 
        acp = PCA(svd_solver='full')
        coord = acp.fit_transform(ds_)

        
        if pca_details:
            print("Input_dim : " + str(ds_.shape[1]) + " ; reduced dim : " + str(coord.shape[1]))
            
            p = acp.n_components_
            plt.plot(np.arange(1,p+1),np.cumsum(acp.explained_variance_ratio_)) 
            plt.title("Explained variance vs. # of factors")
            plt.ylabel("Cumsum explained variance ratio")
            plt.xlabel("Factor number")
            plt.show()
            
            eigval=acp.explained_variance_
            plt.plot(np.arange(1,p+1),eigval) 
            plt.title("Scree plot") 
            plt.ylabel("Eigen values") 
            plt.xlabel("Factor number") 
            plt.show()
            
        ds = pd.DataFrame(coord)
            
            

        
        
    
    #ds = (ds - ds.mean().mean())/ds.std().std()

    X_ = []
    Y_1 = []
    Y_2 = []
    Y_3 = []

    """for i in range(ds.shape[0]-3):
        if i%4==0:
            X_.append(i)
        elif i%4==1:
            Y_1.append(i)
        elif i%4==2:
            Y_2.append(i)
        else:
            Y_3.append(i)"""

    
    for i in range(int((ds.shape[0]-3)/4)):
        X_.append(i)
        Y_1.append(i*2)
        Y_2.append(i*3)
        Y_3.append(i*4)
        


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
    
    if shuffle:
        X, Y = shuffle_together(X, Y)

    X_train = X[:split]
    X_test = X[split:]

    Y_train = Y[:split]
    Y_test = Y[split:]
    
    return X_train, X_test, Y_train, Y_test, sc, acp



def build_mto(split=270, pca=False, pca_details=False, shuffle=False):
    """
    Returns a train/test splitted dataset ready to be converted to tensors for the 
    learning part, but in a many to one architecture.
    Can also perform PCA on the data.
    """  
    
    ds = pd.read_csv("out.csv", header=None)
    
    if pca:
        sc = StandardScaler()
        ds_ = sc.fit_transform(ds) 
        acp = PCA(svd_solver='full')
        coord = acp.fit_transform(ds_)

        
        if pca_details:
            print("Input_dim : " + str(ds_.shape[1]) + " ; reduced dim : " + str(coord.shape[1]))
            
            p = acp.n_components_
            plt.plot(np.arange(1,p+1),np.cumsum(acp.explained_variance_ratio_)) 
            plt.title("Explained variance vs. # of factors")
            plt.ylabel("Cumsum explained variance ratio")
            plt.xlabel("Factor number")
            plt.show()
            
            eigval=acp.explained_variance_
            plt.plot(np.arange(1,p+1),eigval) 
            plt.title("Scree plot") 
            plt.ylabel("Eigen values") 
            plt.xlabel("Factor number") 
            plt.show()
            
        ds = pd.DataFrame(coord)
            
            

        
        
    
    #ds = (ds - ds.mean().mean())/ds.std().std()

    X_ = []
    Y_1 = []
    Y_2 = []
    Y_3 = []

    """for i in range(ds.shape[0]-3):
        if i%4==0:
            X_.append(i)
        elif i%4==1:
            Y_1.append(i)
        elif i%4==2:
            Y_2.append(i)
        else:
            Y_3.append(i)"""

    
    for i in range(int((ds.shape[0]-3)/4)):
        X_.append(i)
        Y_1.append(i*2)
        Y_2.append(i*3)
        Y_3.append(i*4)
        


    X_ds = ds.iloc[X_]
    Y1_ds = ds.iloc[Y_1]
    Y2_ds = ds.iloc[Y_2]
    Y3_ds = ds.iloc[Y_3]

    X_1 = X_ds.to_numpy()
    Y1 = Y1_ds.to_numpy()
    Y2 = Y2_ds.to_numpy()
    Y = Y3_ds.to_numpy()


    X = []

    for i in range(len(Y1)):
        X.append([X_1[i], Y1[i], Y2[i]])
    
    X = np.array(X)
    
    if shuffle:
        X, Y = shuffle_together(X, Y)

    X_train = X[:split]
    X_test = X[split:]

    Y_train = Y[:split]
    Y_test = Y[split:]
    
    
    
    return X_train, X_test, Y_train, Y_test, sc, acp


def shuffle_together(a, b):
    """
    Shuffles the two arrays a and b along their first axis using the same permutation.
    """
    
    assert len(a) == len(b), "cannot shuffle two lists of different lengths"
    shuf_a = np.empty(a.shape)
    shuf_b = np.empty(b.shape)
    shuffling = np.random.permutation(len(a))
    for old, new in enumerate(shuffling):
        shuf_a[new] = a[old]
        shuf_b[new] = b[old]
    return shuf_a, shuf_b
    



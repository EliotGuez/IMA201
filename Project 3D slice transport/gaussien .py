import numpy as np
import matplotlib.pyplot as plt

#%% Calcul de la racine symétrique

def racine(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    P = eigenvectors
    P_inv = np.linalg.inv(P)
    D_sqrt = np.diag(np.sqrt(eigenvalues))
    return P.dot(D_sqrt).dot(P_inv)



#%% Transformation en nuage d points
def Nuage(X):
    return X.reshape(X.shape[0], X.shape[1]*X.shape[2])


#%% nuage de points aléatoires:


X = np.vstack((
        np.random.rand(50,3),
        .25 * np.random.rand(150,3) + np.array([[0,2,2]])
        ))
Y = np.vstack((
        np.random.rand(100,3) + np.array([[2,2,2]]),
        .5 * np.random.rand(100,3) + np.array([[2,0,0]])
        ))
fig = plt.figure(figsize=(10, 10)) 
axis = fig.add_subplot(1, 1, 1, projection="3d")
axis.scatter(X[:,0],X[:,1],X[:,2],c='blue',s=
             
             
             80)
axis.scatter(Y[:,0],Y[:,1],Y[:,2],c='red',s=80)
#afficher la moyenne m1
plt.plot(np.mean(X[:,0]),np.mean(X[:,1]),np.mean(X[:,2]),'.g',markersize=30)
#afficher la variance

plt.show()

#%% Calcul moyenne et variance de X
def moyenne(X):
    return np.mean(X,axis=0)

def variance(X):
    return np.cov(X.T)



# %%
point=np.random.multivariate_normal(moyenne(X),variance(X),len(X))
fig = plt.figure(figsize=(10, 10)) 
axis = fig.add_subplot(1, 1, 1, projection="3d")
axis.scatter(X[:,0],X[:,1],X[:,2],c='blue',s=    
             80)
print(point.mean(axis=0))
axis.scatter(point[:,0],point[:,1],point[:,2],c='red',s=80)
plt.show()
# %%

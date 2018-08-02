from sklearn.cluster import  KMeans
import random as rd
import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
    def __hash__(self):
        hash = 3
        hash = 71 * hash + self.x
        hash = 71 * hash + self.y
        return hash
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.__class__ == other.__class__)
    def __arr__(self):
        return [[self.x, self.y]]

def kmeans_display(X, label):
    K = np.amax(label) + 1
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    X3 = X[label == 3, :]
    X4 = X[label == 4, :]

    plt.plot(X0[:, 0], X0[:, 1], 'g^', markersize=4, alpha=.8)
    plt.plot(X1[:, 0], X1[:, 1], 'b+', markersize=4, alpha=.8)
    plt.plot(X2[:, 0], X2[:, 1], 'bs', markersize=4, alpha=.8)
    plt.plot(X3[:, 0], X3[:, 1], 'rx', markersize=4, alpha=.8)
    plt.plot(X4[:, 0], X4[:, 1], 'ro', markersize=4, alpha=.8)

    plt.axis('equal')
    plt.plot()
    plt.show()

def genRamdomPoint( n ):
    result = np.array([[0, 0]])
    sets = set()
    i = 0
    while i < n:
        x = rd.randint(0, 1000)
        y = rd.randint(0, 1000)
        temp = Point(x, y)
        if temp not in sets:
            i += 1
            result = np.concatenate((result, temp.__arr__()), axis=0)
            sets.add(temp)
    return np.delete(result, 0, 0)

if __name__ == "__main__":
    X = genRamdomPoint(1000)
    print(X)
    kmeans = KMeans(n_clusters=5, random_state= 0).fit(X)
    kmeans_display(X, kmeans.labels_)
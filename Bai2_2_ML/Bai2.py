from sklearn.cluster import  KMeans
import random as rd
import numpy as np

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
    kmeans = KMeans(n_clusters=5, random_state= 0).fit(X)
    fw = open("output.txt", "w", encoding="utf8")
    for elem in X:
        s = "- Point(%d,%d) in cluster: %d\n" % (elem[0], elem[1], kmeans.predict([elem]))
        fw.write(s)
    fw.close()
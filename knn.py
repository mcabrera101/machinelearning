
from collections import Counter

import numpy as np

class KNN:
    """Machinge learning algorything using the nearest neighbor technique"""
    def __init__(self, k=3):
        self.k = k
        self.independents = 0
        self.dependent = 0

    def euclidean_distance(self, test, train):
        distance = 0
        index = 0

        for i in range(len(test)):
            index = train[0]
            if i != 0:
                a = test[i]
                b = train[i]
                distance = distance + np.square(a - b)

        return np.sqrt(distance), index

    def store(self, trainx, trainy):
        self.independents = trainx
        self.dependent = trainy

    def predict(self, test):
        # Predict the class label based on the test data 
        #prediction = [self._predict(data) for name, data in test.items()]
        # find the distance between the points
        distances = np.empty([28, 112], dtype = object)
        col = 0
        row = 0
        for i in test.itertuples():
            col = 0
            for j in self.independents.itertuples():
                distances[row][col] = self.euclidean_distance(i, j)
                col = col + 1
            row = row + 1
        # sort distances and return the index of the closest k neighbors
        distances_sorted = np.sort(distances)


        d = np.delete(distances_sorted, np.s_[self.k:111], 1)
        k_index = []
        for i in d:
            for s in i:
                k_index.append(s[1])

        '''
        index = 0
        temp = 1000
        indecies = []
        for i in range(row):
            for j in range(col):
                if temp > distances[i][j]:
                    temp = distances[i][j]
                    index = j
            indecies[i] = j
        '''
        return None
        '''

    def asses(self, prediction, test):
        pass

from collections import Counter

import numpy as np

class KNN:
    """Machinge learning algorything using the nearest neighbor technique"""
    def __init__(self, k=3):
        self.k = k

    def euclidean_distance(x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))
    def store(self,trainingSet):
        self.independent = trainingSet['City Services Availability', 'Housing Cost', 'Quality of schools', 'Community trust in local police',
                         'Community Maintenance', 'Availability of Community Room ']
        self.dependent = trainingSet['Unhappy/Happy']
    def predict(self,test):
        pass
    def asess(self,prediction,test):
        pass
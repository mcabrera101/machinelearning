import pandas as pd
from scipy.stats import pearsonr
import numpy as np
from itertools import cycle

correlation_matrix = np.empty([7, 7])

#Task2
raw_features = pd.read_csv('HappinessData-1.csv')
print(raw_features)
features = raw_features[['City Services Availability', 'Housing Cost', 'Quality of schools', 'Community trust in local police', 'Community Maintenance', 'Availability of Community Room ', 'Unhappy/Happy']] # rearrange column here
features.to_csv('HappinessData-1.csv', index=False)

#Task3
last_column = features.iloc[-1, :]
#print(last_column)
for feature in features:
    it = iter(features)
    #print(it)
    features[feature] = features[feature].fillna(int(features[feature].mean()))
    try:
        while (True):

            correlation_matrix[feature,], _ = pearsonr(features[feature], features[next(it)])
    except StopIteration:
        print(corr)
    """""
    if feature != 'Unhappy/Happy':
       corr, _ = pearsonr(features[feature], features[next(it)])
    if feature != "Housing Cost":
        corr, _ = pearsonr(features["Housing Cost"], features[next(it)])
        print(corr)
"""



features.to_csv('HappinessData-1.csv', index=False)

#task4

#print(corr)
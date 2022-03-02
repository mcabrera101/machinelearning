import pandas as pd
from scipy.stats import pearsonr
import numpy as np


correlation_matrix = np.empty([7, 7], dtype = object)

#Task2
raw_features = pd.read_csv('HappinessData-1.csv')
print(raw_features)
features = raw_features[['City Services Availability', 'Housing Cost', 'Quality of schools', 'Community trust in local police',
                         'Community Maintenance', 'Availability of Community Room ', 'Unhappy/Happy']] # rearrange column here
features.to_csv('HappinessData-1.csv', index=False)

#Task 3 and 4

index = 0
for feature in features:
    it = iter(features)
    #print(it)
    features[feature] = features[feature].fillna(int(features[feature].mean()))
    correlation_matrix[0, index], _ = pearsonr(features["City Services Availability"], features[feature])
    correlation_matrix[1, index], _ = pearsonr(features["Housing Cost"], features[feature])
    correlation_matrix[2, index], _ = pearsonr(features['Quality of schools'], features[feature])
    correlation_matrix[3, index], _ = pearsonr(features['Community trust in local police'], features[feature])
    correlation_matrix[4, index], _ = pearsonr(features['Community Maintenance'], features[feature])
    correlation_matrix[5, index], _ = pearsonr(features['Availability of Community Room '], features[feature])
    correlation_matrix[6, index], _ = pearsonr(features['Unhappy/Happy'], features[feature])
    index = index + 1

features.to_csv('HappinessData-1.csv', index=False)



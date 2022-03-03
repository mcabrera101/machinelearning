# Miguel Cabrera

import pandas as pd
from scipy.stats import pearsonr
import numpy as np
from knn import KNN
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
cmap = ListedColormap(["#FF0000", "#00FF00"])

correlation_matrix = np.empty([7, 7], dtype = object)

#Task2
raw_features = pd.read_csv('HappinessData-1.csv')
print(raw_features)
features = raw_features[['City Services Availability', 'Housing Cost', 'Quality of schools', 'Community trust in local police',
                         'Community Maintenance', 'Availability of Community Room ', 'Unhappy/Happy']] # rearrange column here
features.to_csv('HappinessData-1.csv', index=False)
print(features)
#Task 3 and 4


index = 0
for feature in features:
    it = iter(features)
    #print(it)
    features[feature] = features[feature].fillna(int(features[feature].mean()))
    correlation_matrix[0, index], _ = pearsonr(features['City Services Availability'], features[feature])
    correlation_matrix[1, index], _ = pearsonr(features['Housing Cost'], features[feature])
    correlation_matrix[2, index], _ = pearsonr(features['Quality of schools'], features[feature])
    correlation_matrix[3, index], _ = pearsonr(features['Community trust in local police'], features[feature])
    correlation_matrix[4, index], _ = pearsonr(features['Community Maintenance'], features[feature])
    correlation_matrix[5, index], _ = pearsonr(features['Availability of Community Room '], features[feature])
    correlation_matrix[6, index], _ = pearsonr(features['Unhappy/Happy'], features[feature])
    index = index + 1

features.to_csv('HappinessData-1.csv', index=False)
print(features.shape)

'''plt.figure()
plt.scatter(features['City Services Availability'], features['Housing Cost'], c=features['Unhappy/Happy'], cmap=cmap,
            edgecolor='k', s=20)
plt.show()'''
k = 5

trainI, testI, trainD, testD = train_test_split(features.iloc[:, 0:6], features.iloc[:, 6], test_size=0.2, random_state=777)
'''
train = features.iloc[29:140, :]
trainI = features.iloc[29:140, 0:5]
trainD = features.iloc[29:140, 6]
testI = features.iloc[1:28, 0:5]
testD = features.iloc[1:28, 6]
'''
model = KNN(k)
model.store(trainI, trainD)
prediction = model.predict(testI)
#d = model.euclidean_distance(features['City Services Availability'], features['Housing Cost'])
print(prediction)

#Task 6
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(trainI, trainD)
knn.predict(testI)

#Testing knn with different values of k
"""
errorRate = np.empty([50], dtype = object)
correct = 0
for i in range(50):
    model = KNN(i)
    model.store(trainI, trainD)
    prediction = model.predict(testI)
    for i in range(len(train.index)):
        if trainD == classified
            correct = correct + 1
    errorRate[i] = correct/len(train.index)

x = range(50)
y = errorRate
plt.plot(x, y)
plt.xlabel('K')
plt.ylabel('Error Rate') 
plt.title('Error Rate vs K') 
plt.show()

"""

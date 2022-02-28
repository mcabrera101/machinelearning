import pandas as pd
from scipy.stats import pearsonr

#Task2
df = pd.read_csv('HappinessData-1.csv')
print(df)
df_reorder = df[['City Services Availability', 'Housing Cost', 'Quality of schools', 'Community trust in local police', 'Community Maintenance', 'Availability of Community Room ', 'Unhappy/Happy']] # rearrange column here
df_reorder.to_csv('HappinessData-1.csv', index=False)

#Task3
for i in df_reorder:
    df_reorder[i] = df_reorder[i].fillna(int(df_reorder[i].mean()))

df_reorder.to_csv('HappinessData-1.csv', index=False)

#task4
corr, _ = pearsonr(df_reorder['Housing Cost'], df_reorder['Unhappy/Happy'])
#for i
#corr[i] = pearsonr(df_reorder["City Services Availability"],df_reorder["Housing Cost"])
print(corr)
import pandas as pd

#Task2
df = pd.read_csv('HappinessData-1.csv')
print(df)
df_reorder = df[['City Services Availability', 'Housing Cost', 'Quality of schools', 'Community trust in local police', 'Community Maintenance', 'Availability of Community Room ', 'Unhappy/Happy']] # rearrange column here
df_reorder.to_csv('HappinessData-1.csv', index=False)

#Task3
for i in df_reorder:
    df_reorder[i] = df_reorder[i].fillna(float("{:,.2f}".format(df_reorder[i].mean())))

df_reorder.to_csv('HappinessData-1.csv', index=False)
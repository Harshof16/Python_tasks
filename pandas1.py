# Task: from the github repos csv file, cleanse the data and show in plotly (graphs), also save it in csv

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('github_repos.csv')

print('Total repos', len(df))
print('Total stars:', df['Stars'].sum())
print('Average stars per repo:', round(df['Stars'].mean(),2))

print('\n Top most starred repositories : ', )
print(df[['Name','Stars']].sort_values(by='Stars', ascending=False).head())

# count of repos per language
lang_counts = df['Language'].value_counts()
print('\n Language Distribution: ')
print(lang_counts)

lang_counts.plot(kind='bar',title='Repository count by language',color='skyblue')
plt.xlabel('Language')
plt.ylabel('Number of repositories')
plt.tight_layout()
plt.show()

# save top 5 to csv
df[['Name','Stars']].sort_values(by='Stars', ascending=False).head().to_csv('top_repos.csv', index=False)

# filter repos more than 500 stars
popular_repos = df[df['Stars'] > 500]
print(popular_repos[['Name','Stars']])

# Group by language and sum stars
lang_summary = df.groupby('Language')[['Stars','Forks']].sum().sort_values(by='Stars', ascending=False)
print(lang_summary)

# create a new column
df['start_to_fork_ratio'] = df['Stars']/(df['Forks'] + 1)
print(df[['Name', 'start_to_fork_ratio']].sort_values(by='start_to_fork_ratio', ascending=False).head(5))

# updated repos by sorting
df['updated_repos'] = pd.to_datetime(df['Last Modified'])       # make sure it's datetime
recent_mask = df['updated_repos'] > (pd.Timestamp.now(tz='UTC') - pd.Timedelta(days=90))
recent = df.loc[recent_mask, ['Name', 'updated_repos']]         # The df.loc accessor in pandas is used to access a group of rows and columns by labels or a boolean array. It is one of the primary ways to select data in a DataFrame
print(recent)

# plot top 10 repos by stars
top10 = df.sort_values(by='Stars', ascending=False).head(10)
ax = top10.plot(x='Name',y='Stars',kind='bar',title='Repository count by language',color='orange')
for container in ax.containers:
    ax.bar_label(container, label_type='edge')
plt.tight_layout()
plt.show()






import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('internet_usage.csv')

df.info()
var = df.columns
df = df.drop(columns=['Country Code'])
df = df.replace({'..':0})
df[df.columns[1:]] = df[df.columns[1:]].apply(pd.to_numeric, errors='coerce')
df.info()

cols = ['Country Name','2000', '2001', '2002', '2003', '2004','2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022','2023']

for features in cols:
    if features in df.columns:
        plt.figure(figsize=(12,5))
        sns.histplot(df[features].dropna(),color='purple',kde=True)
        plt.title(f'Histogram of {features}')
        plt.xlabel(features)
        plt.ylabel('Count')
        plt.tight_layout()
        plt.show()

cols = ['2000', '2001', '2002', '2003', '2004','2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013',
       '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022','2023']

for features in cols:
    if features in df.columns:
        plt.figure(figsize=(12,5))
        sns.lineplot(df[features].dropna(),marker='o',color='purple')
        plt.title(f'Count plot of {features}')
        plt.xlabel(features)
        plt.ylabel("count")
        plt.tight_layout()
        plt.show()

if set(cols).issubset(df.columns):
    sns.pairplot(df[cols].dropna(),diag_kind='kde')
    plt.show()
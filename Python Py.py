# -*- coding: utf-8 -*-
"""Influur.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hp1knmvZ_UKvtfXzzRy7_E7w6gLrKBs5

### Dataset exploration
"""

import pandas as pd

df = pd.read_csv('Business Analyst Challenge Influur.csv')

df[df["STATUS"]=="DELIVERED"]

df.info()

df.describe()

df['ID'].nunique()
# len(pd.unique(df['height']))

df['CP'].unique()

df.groupby(['MOTIVE','STATUS'])['INTEREST_RATE'].mean()
df.groupby(['CP','STATUS'])['ID'].count()
df['TXN'].count()

df.groupby(['STATUS'])['INTEREST_RATE'].mean()

"""### Add a "NO REPLY" status"""

df.loc[df["STATUS"].isnull() & df["TXN"].isnull(), 'STATUS'] = "NO REPLY"

df[df["STATUS"] == 'NO REPLY'].count()

#df.loc[df["STATUS"].isnull() & df["TXN"].isnull(), 'STATUS'] = "NO REPLY"
# df[df["STATUS"].isnull() & df["TXN"].isnull()]
# df[df["TXN"].isnull() & df["STATUS"] == 'NO REPLY']

"""### Understand UPDATE values and possible calculations with window functions"""

df["UPDATE"] = df["UPDATE"].str.slice(stop=5)
df.head()

df[df["UPDATE"] == '00:00.0']

# df['PREVIOUS_UPDATE'] = df['UPDATE'].rolling(1)
# df['PREVIOUS_UPDATE'] = df.groupby(['ID', 'UPDATE']).df['UPDATE']


# orders = df[['ID', 'UPDATE','STATUS']]
orders = df.sort_values(by=['ID','UPDATE'])
orders['lagged_update'] = df.groupby(['ID'])['UPDATE'].shift(-1)

orders.head(10)

"""### Profiling the dataframe"""

pip install pandas-profiling

#Correlation and more descriptive analysis to be used to answer Bs Qs
import pandas as pd
from pandas_profiling import ProfileReport

report = pd.DataFrame(df)

# Generate a profile report
profile = ProfileReport(report)
profile.to_file("data_profile_report.html")
profile.to_notebook_iframe()
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os
import pandas as pd
import seaborn as sns
import time


raw_data = pd.read_excel('data.xlsx', engine='openpyxl')
df = raw_data.copy()

# Fill Merged cells with precinct numbers, and assign them as indexes
df["PCT"] = raw_data["PCT"].fillna(method='ffill', axis = 0)
df.set_index('PCT', inplace=True)



"""
Total Major Felonies by Precinct
"""
# Get only total major felonies
df1 = df.iloc[7::8]

# Drop type of crime categorization, and DOC precinct
df1.drop(columns=["CRIME"], axis=1, inplace=True)
df1.drop('DOC', axis=0, inplace=True)

# Make sure all columns (years) are of numeric value
df1.columns = pd.to_numeric(df1.columns)

precincts = df1.copy()

# x = precinct, y = number of major felonies
precincts = precincts.T

precincts.plot(figsize=(20,10), alpha=0.7)

plt.title('Total Major Felonies by Precinct (2000 ~ 2022)', fontsize=20)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, fontsize=7, ncol=2)

plt.xlabel('Years (2000 ~ 2022)', fontsize=12)
plt.ylabel('Total Major Felonies', fontsize=12)

plt.xticks(precincts.index.values)

#plt.ylim([0, 7000])
plt.margins(x=0)

plt.grid()
#plt.show()


"""
NYC Boroughs 
Manhattan = 1~34
Bronx = 40~52
Brooklyn = 60~94
Queens = 100~115
Staten = 120~123
"""
boroughs = pd.DataFrame(index=['Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'Staten'], columns=df1.columns)
boroughs.loc['Manhattan'] = df1.loc[1:34].mean().round().values
boroughs.loc['Bronx'] = df1.loc[40:52].mean().round().values
boroughs.loc['Brooklyn'] = df1.loc[60:94].mean().round().values
boroughs.loc['Queens'] = df1.loc[100:115].mean().round().values
boroughs.loc['Staten'] = df1.loc[120:123].mean().round().values

print(boroughs)

# x = borough, y = number of major felonies
boroughs = boroughs.T

boroughs.plot(figsize=(20, 10), alpha=0.7)

plt.title('Average Major Felonies by Borough (2000 ~ 2022)', fontsize=20)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, fontsize=10)

plt.xlabel('Years (2000 ~ 2022)', fontsize=12)
plt.ylabel('Average Major Felonies', fontsize=12)

plt.xticks(boroughs.index.values)

#plt.ylim([0, 7000])
plt.margins(x=0)

plt.grid()
plt.show()
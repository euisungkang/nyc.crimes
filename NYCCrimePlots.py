import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class NYCCrimePlots :
    def __init__(self) :

        # Get raw data from NYC website
        raw_data = pd.read_excel('data.xlsx', engine='openpyxl')
        df = raw_data.copy()

        # Fill Merged cells with precinct numbers
        df["PCT"] = raw_data["PCT"].fillna(method='ffill', axis = 0)

        self.df = df

    """
    Average Major Felonies by Crime
    """
    def avgFeloniesbyCrime(self) :
        df1 = self.df.copy()

        # Drop precinct categorization, and DOC precinct
        df1 = df1[df1.PCT != 'DOC']
        df1.drop(columns=['PCT'], axis=1, inplace=True)

        # Drop total crime data
        df1 = df1[df1.index % 8 != 7]

        # Get sum of every type of crime
        crimes = df1.groupby(df1['CRIME']).mean().round()

        # x = crime type, y = average number of major felonies
        crimes = crimes.T

        # Create Grid
        crimes.plot(figsize=(20,0), alpha=0.7)
        plt.title('Average Major Felonies by Crime (2000 ~ 2022)', fontsize=20, pad=40)
        plt.legend(bbox_to_anchor=(0, 1.05), loc='upper left', borderaxespad=1, ncol = 7, fontsize=8, columnspacing=-5)
        plt.xlabel('Years (2000 ~ 2022)', fontsize=12)
        plt.ylabel('Average Major Felonies', fontsize=12)
        plt.margins(x=0)
        plt.grid()

        return crimes

    """
    Total Major Felonies by Precinct
    """
    def totalFeloniesbyPrecinct(self) :
        # Get only total major felonies
        df1 = self.df.copy()
        df1.set_index('PCT', inplace=True)
        df1 = df1.iloc[7::8]

        # Drop type of crime categorization, and DOC precinct
        df1.drop(columns=["CRIME"], axis=1, inplace=True)
        df1.drop('DOC', axis=0, inplace=True)

        # Make sure all columns (years) are of numeric value
        df1.columns = pd.to_numeric(df1.columns)

        precincts = df1.copy()

        # x = precinct, y = number of major felonies
        precincts = precincts.T

        # Create Grid
        precincts.plot(figsize=(20,10), alpha=0.7)
        plt.title('Total Major Felonies by Precinct (2000 ~ 2022)', fontsize=20, pad=30)
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, fontsize=7, ncol=2)
        plt.xlabel('Years (2000 ~ 2022)', fontsize=12)
        plt.ylabel('Total Major Felonies', fontsize=12)
        plt.xticks(precincts.index.values)
        plt.margins(x=0)
        plt.grid()

        return precincts

    """
    Average Major Felonies by Borough
        NYC Boroughs 
        Manhattan = 1~34
        Bronx = 40~52
        Brooklyn = 60~94
        Queens = 100~115
        Staten = 120~123
    """
    def avgFeloniesbyBorough(self) :
        # Get only total major felonies
        df1 = self.df.copy()
        df1.set_index('PCT', inplace=True)
        df1 = df1.iloc[7::8]

        # Drop type of crime categorization, and DOC precinct
        df1.drop(columns=["CRIME"], axis=1, inplace=True)
        df1.drop('DOC', axis=0, inplace=True)

        # Make sure all columns (years) are of numeric value
        df1.columns = pd.to_numeric(df1.columns)

        boroughs = pd.DataFrame(index=['Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'Staten'], columns=df1.columns)
        boroughs.loc['Manhattan'] = df1.loc[1:34].mean().round().values
        boroughs.loc['Bronx'] = df1.loc[40:52].mean().round().values
        boroughs.loc['Brooklyn'] = df1.loc[60:94].mean().round().values
        boroughs.loc['Queens'] = df1.loc[100:115].mean().round().values
        boroughs.loc['Staten Island'] = df1.loc[120:123].mean().round().values

        # x = borough, y = average number of major felonies
        boroughs = boroughs.T

        # Create Grid
        boroughs.plot(figsize=(20, 10), alpha=0.7)
        plt.title('Average Major Felonies by Borough (2000 ~ 2022)', fontsize=20, pad=30)
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0, fontsize=10)
        plt.xlabel('Years (2000 ~ 2022)', fontsize=12)
        plt.ylabel('Average Major Felonies', fontsize=12)
        plt.xticks(boroughs.index.values)
        plt.margins(x=0)
        plt.grid()

        return boroughs
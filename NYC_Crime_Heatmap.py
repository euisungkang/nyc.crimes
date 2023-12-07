from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os
import pandas as pd
import seaborn as sns
import geopandas as gpd
import geodatasets
from shapely.wkt import loads
import time
import os
os.system("clear")

from NYCCrimePlots import NYCCrimePlots

class NYCCrimeHeatmap :
    def precinctHeatmap(self, df) :

        # Read Geo Shapes of all Precincts of NYC
        # Based on Police Precincts on NYC Open Data
        nypp_path = "./nypp.csv"
        precs = gpd.read_file(nypp_path)
        precs.set_index('Precinct', inplace=True)

        # Convert WKT Format to MultiPolygon format
        precs.geometry =  precs['the_geom'].apply(loads)

        # Make sure all indices to compare are of numeric value
        precs.index = pd.to_numeric(precs.index)
        df.index = pd.to_numeric(df.index)
        df.index.name = "Precinct"      # default index of 'PCT'

        map_and_stats = precs.merge(df, on="Precinct")

        fig, ax = plt.subplots(1, figsize=(8, 8))
        
        plt.title('Crimes in NYC by Precinct', fontsize=20, pad=30)

        bar_info = plt.cm.ScalarMappable(cmap="Reds", norm=plt.Normalize(vmin=0, vmax=3000))
        bar_info._A = []
        cbar = fig.colorbar(bar_info, ax=ax)
    
        plt.xticks(rotation=90)
        plt.axis('off')

        map_and_stats.plot(column=2010, cmap="Reds", linewidth=0.4, ax=ax, edgecolor=".4")
    
    def boroughHeatmap(self, df) :

        # Read Geo Shapes of all Boroughs from geodatasets module
        nybb_path = geodatasets.get_path("nybb")
        boros = gpd.read_file(nybb_path)

        # Name of Boroughs will be merge point
        boros.set_index('BoroName', inplace=True)
        df.index.name = "BoroName"

        map_and_stats = boros.merge(df, on="BoroName")

        fig, ax = plt.subplots(1, figsize=(8, 8))
        
        plt.title('Crimes in NYC by Borough', fontsize=20, pad=30)

        bar_info = plt.cm.ScalarMappable(cmap="Reds", norm=plt.Normalize(vmin=0, vmax=3000))
        bar_info._A = []
        cbar = fig.colorbar(bar_info, ax=ax)
    
        plt.xticks(rotation=90)
        plt.axis('off')

        map_and_stats.plot(column=2010, cmap="Reds", linewidth=0.4, ax=ax, edgecolor=".4")


if __name__ == '__main__' :

    plots = NYCCrimePlots()
    heatmap = NYCCrimeHeatmap()

    borough = plots.avgFeloniesbyBorough()
    borough = borough.T
    heatmap.boroughHeatmap(borough)
    
    precinct = plots.totalFeloniesbyPrecinct()
    precinct = precinct.T
    heatmap.precinctHeatmap(precinct)

    plt.show()
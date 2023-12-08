import matplotlib.pyplot as plt
from NYCCrimePlots import Plots 
from NYCCrimeHeatmap import Heatmap
from RelevantNews import News
import os
os.system('clear')

if __name__ == '__main__' :
    news = News()
    #result = news.search("Staten Island", "Crimes", "2012")

    plots = Plots()
    # heatmap = Heatmap()

    borough = plots.avgFeloniesbyBorough()
    borough = borough.T
    #heatmap.boroughHeatmap(borough)
    
    # precinct = plots.totalFeloniesbyPrecinct()
    # precinct = precinct.T
    # heatmap.precinctHeatmap(precinct)

    # crimes = plots.avgFeloniesbyCrime()

    plt.show()
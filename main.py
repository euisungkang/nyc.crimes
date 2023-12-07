import matplotlib.pyplot as plt
from NYCCrimePlots import NYCCrimePlots 
from NYCCrimeHeatmap import NYCCrimeHeatmap

if __name__ == '__main__' :
    plots = NYCCrimePlots()
    heatmap = NYCCrimeHeatmap()

    borough = plots.avgFeloniesbyBorough()
    borough = borough.T
    heatmap.boroughHeatmap(borough)
    
    precinct = plots.totalFeloniesbyPrecinct()
    precinct = precinct.T
    heatmap.precinctHeatmap(precinct)

    crimes = plots.avgFeloniesbyCrime()

    plt.show()
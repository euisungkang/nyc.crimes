<h1 align="center">
  <br>
  <a href="https://github.com/euisungkang/NYC-Crime-Analysis"><img src="https://i.ibb.co/xXdbt0S/Wide-HD.png" alt="NYC Illustration"></a>
  <br>
  NYC Major Felony Offenses 
  <br>
</h1>

<p align="center">
  <a href="https://www.python.org/">
     <img alt="python" src="https://img.shields.io/badge/py-3.12%20%7C%203.11%20%7C%203.10%20%7C%203.9-3572a5">
  </a>
  <a href="https://pypi.org/">
    <img alt="pypi" src="https://img.shields.io/badge/pypi-0.2.0-3572a5">
  </a>
  <a href="https://numpy.org/">
    <img alt="numpy" src="https://img.shields.io/badge/numpy-1.21.0-3572a5">
  </a><br>
  <a href="https://pypi.org/project/shapely/">
    <img alt="shapely" src="https://img.shields.io/badge/shapely-2.0.2-3572a5">
  </a>
  <a href="https://matplotlib.org/stable/">
    <img alt="matplotlib" src="https://img.shields.io/badge/matplotlib-3.8.2-3572a5">
  </a>
  <a href="">
    <img alt="geopandas" src="https://img.shields.io/badge/geopandas-0.14.1-169959">
  </a>
</p>

<p align="center">
  <a href="#usage">Usage</a>
  •
  <a href="#visualizations">Visualizations</a>
  •
  <a href="#data source">Data Source</a>
  •
  <a href="#contributing">Contributing</a>
  •
  <a href="#license">License</a>
</p>

# Overview
The objective behind this project is to offer a valuable resource for both the general public and stakeholders interested in the historical patterns of major felony offenses in NYC. Although [NYC Open Data](https://opendata.cityofnewyork.us/) releases a majority of its data to the public, there haven't been any extensive visualizations and analysis on major felony offenses since 2018. Thus, with the latest available data, I aim to contribute to a better understanding of the city's safety landscape over the past two decades.

# Visualizations

<!-- ### Total Major Felonies by Precinct
<figure>
  <img alt="Total Felonies by Precinct Plot" src="Plots/Total-Felonies-by-Precinct.png">
  <figcaption>Line plot showcasing the trend of total number of major felonies in each precinct from 2000 ~ 2022</figcaption>
</figure>

One of the first visualizations using the raw data provided is the Total Number of Major Felonies by Precinct over 22 years. At first glance, it's difficult to pinpoint any specific patterns. Perhaps, we can note that the general trend of major felony offenses has been on a downhill trend since 2000, with an uphill starting 2021. However, each of the 77 precincts in NYC has its own trend, and it's near impossible to distinguish between each one in the visualization. <br><br>
Let's try a better approach starting from a larger set of precincts: boroughs -->

### Average Major Felonies by Borough
```python
from NYCCrimePlots import NYCCrimePlots

plots = NYCCrimePlots()
precinct = plots.totalFeloniesbyPrecinct()

precinct
```
<figure>
  <img alt="Total Felonies by Precinct Plot" src="Plots/Average-Felonies-by-Borough.png">
  <figcaption>Line plot showcasing the trend of average number of major felonies in each borough from 2000 ~ 2022</figcaption>
</figure>

Immediately, we can notice the previous general patterns:
1. Major felony offenses are on a general decline since 2000
2. Major felony offenses are on an incline from 2021

However, we can also notice specific patterns such as Staten Island having a spike of offenses in 2012.<br>Let's take a closer look.

<figure>
  <img alt="Staten Island Zoomed" src="Plots/Staten-Island-Zoomed.png" style="width: 50%">
  <figcaption>Staten Island borough in 2012</figcaption>
</figure>



Categorizing the precincts into NYC's five boroughs provides a far simpler visualization. *Note, there is the caveat that minute patterns of a precinct are lost, which is addressed further on.*

<!-- 
#### Heatmap by Precinct
<figure>
<img alt="Total Felonies by Precinct Plot" src="Plots/Precinct-Heatmap.png" style="width:50%">
  <figcaption>Heatmap visualizations offering an at-a-glance view of major felonies distribution across precincts</figcaption>
</figure>

#### Heatmap by Borough
<figure>
  <img alt="Total Felonies by Precinct Plot" src="Plots/Borough-Heatmap.png" style="width:50%">
  <figcaption>Heatmap visualizations offering an at-a-glance view of major felonies distribution across boroughs</figcaption>
</figure>

### Average Major Felonies by Crime
<figure>
  <img alt="Total Felonies by Precinct Plot" src="Plots/Average-Felonies-by-Crime.png">
  <figcaption>Line plot showcasing the trend of average number of crimes by each felony type from 2000 ~ 2022</figcaption>
</figure> -->

# Usage
To run the program and generate the visualizations, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/euisungkang/nyc-major-felonies.git
   ```
2. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the main script**
    ```bash
    python main.py
    ```

Make sure you have Python installed on your machine, and consider using a virtual environment to manage dependencies. Adjust the commands based on your project structure and requirements.

# Data Source
The data is sourced from the [NYC Open Data](https://opendata.cityofnewyork.us/), and released by the [NYPD](https://www.nyc.gov/site/nypd/stats/crime-statistics/historical.page). The dataset spans from the year 2000 to 2022, providing a comprehensive view of major felony offenses in New York City.

# Contributing
If you'd like to contribute to this project, please check out our [contribution guidelines](CONTRIBUTING.md).

# License

Artwork created by [Midjourney AI](https://www.midjourney.com/explore).

Released under the [MIT](LICENSE) license.
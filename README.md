CSE 163 FINAL:
- You should write instructions for us to run your project to reproduce your results. Tell us which Python modules to run to get your results and anything else we need to do to run them.

- If there is anything we need to do to set up your project, like install libraries or how to download your data (if you did not submit it), give us instructions for how to do so.

- Anything else we need to know about running your project!

Must be DETAILED enough that your mentor can run your code.

newAnalysis.py:

about the line graph:
This file contains all of the code from Exisiting_Bike_Facilities to make a line plot that shows the num of bike infrastructures built between 2010-2021. These years are chosen because it has data from the past 10 years and it would be reliable to use years that are recent to get an accurate and precise graph. The line plot has a legend on the top right-hand corner to allow the user to understand the different bike infrastructures and the lines that are being graphed. The plot is graphed in an up and down line because it represents the number of bike infrastructures built during the year, the line going down means that few or no bike infrastructures were being built. While the line going up means that more bike infrastructures were being built. We tried to sum up the number of bike infrastructures being built through the years 2010-2021, but we ran into a problem of not being able to work with the dataset since it contains data that cannot be groupby by the number of bike infrastructures and sum it. This is a messy dataset that requires filters and new columns to be added. We felt that the line going up and down shows a more accurate visualization of the number of bike infrastructure building progress.

about the line graph code:
To produce the line graph, we first read in the CSV file using pandas and parsed the CSV by the INSTALL_DATE. The INSTALL_DATE is when the bike infrastructure was first built. We then made another column to keep track of the number of the different bike infrastructures in the years, so that we can use the number later to produce the number of bike infrastructures being built between 2010-2021. Once we have a new column made for the number of bike infrastructures, we use groupby to sum the number of bike infrastructures. After we filter the data frame based on the years that we want 2010-2021. Finally, we plot the graph based on the INSTALL_DATE and NUM (the number of bike infrastructures) and categorize it based on CATEGORY (different bike infrastructures). The line plot is saved in a file called bike_infrastructures_plot.


about the map:

The second part of the file contains code to map the different bike infrastructures being built through the pass 2 years between 2010-2021. We did the pass 2 years because the results of the pass 4 years show the same bike infrastructures from the pass and there isn't any differences. When we did between 2012-2014, there is quite a few different bike infrastructures being built during these time, when we try to compare it from 2011-2014, the bike infrastructures is similar to 2010. This tells us that there wasn't any changed in the number of bike infrastructures. This goes for the same between 2015-2018 and 2019-2021, these graphs represent the number of bike infrastructures built between these times.

about the map code:

For the map code we use data from the Planned_Bike_Facilities, then the Existing_Bike_Facilities dataset because the Planned_Bike_Facilities allows us to create graphs with it's .shp file. Also the Planned_Bike_Facilities are data from the supported development of short and long term use bike infrastructures in the Great Seattle Area. We firsted read in the file using geopandas.readfile(). We plotted the dataframe without filtering to use as a based for plotting the different bike infrastructures throughout the year. This is a method that is similar to A5, where we colored the WA_data grey that we can fill in the rest of the states. For each year, we filter the column INSTALL_DA by the date of the year that we wanted. INSTALL_DA is the data where the bike infrastructure was first built. For the plots where we wanted to filter it between 2012-2014, we manual have to set the dataframe == to the year that we wanted. This is because we ran into a problem where the dates are strings. After we a plot all of the graphs onto one file to allow the user to get an overview of the different bike infrastructures being throughout the years.
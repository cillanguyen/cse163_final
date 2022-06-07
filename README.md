CSE 163 FINAL:
- You should write instructions for us to run your project to reproduce your results. Tell us which Python modules to run to get your results and anything else we need to do to run them.

- If there is anything we need to do to set up your project, like install libraries or how to download your data (if you did not submit it), give us instructions for how to do so.

- Anything else we need to know about running your project!

Must be DETAILED enough that your mentor can run your code.


--AQUIRING DATA--

All of the data we used can be found at the following Seattle governmental websites. Each page has options to download the data as CSV, SHP (if applicable), and other formats.


Existing Bike Facilities (CSV): https://data.seattle.gov/dataset/Existing-Bike-Facilities/
cd3j-uiyc#

Planned Bike Facilities (CSV): https://data.seattle.gov/dataset/Planned-Bike-Facilities/t8ug-huzv

Bike Counter Datasets (CSV):
    
   - Fremont Bridge: https://data.seattle.gov/Transportation/Fremont-Bridge-Bicycle-Counter/65db-xm6k

   - Spokane St. Bridge: https://data.seattle.gov/Transportation/Spokane-St-Bridge-Bicycle-Counter/upms-nr8w

   - Broadway: https://data.seattle.gov/Transportation/Broadway-Cycle-Track-North-Of-E-Union-St-Bicycle-C/j4vh-b42a
    
   - Chief Sealth Trail: https://data.seattle.gov/Transportation/Chief-Sealth-Trail-North-of-Thistle-Bicycle-Counte/uh8h-bme7
    
   - Elliot Bay Trail: https://data.seattle.gov/Transportation/Elliott-Bay-Trail-in-Myrtle-Edwards-Park-Bicycle-a/4qej-qvrz
    
   - Burke-Gilman Trail: https://data.seattle.gov/Transportation/Burke-Gilman-Trail-north-of-NE-70th-St-Bicycle-and/2z5v-ecg8
    
   - Mountains-To-Sound Trail: https://data.seattle.gov/Transportation/MTS-Trail-west-of-I-90-Bridge-Bicycle-and-Pedestri/u38e-ybnc
    
   - 2nd Avenue: https://data.seattle.gov/Transportation/2nd-Ave-Cycle-Track-North-of-Marion-St-Bicycle-Cou/avwm-i8ym
    
   - Westlake: https://data.seattle.gov/Transportation/Westlake-PBL-at-Newton-St-Bicycle-Counter/675b-cqew

We also renamed the data files to simply the street each bike counter is on,
with underscores for spaces.


--1: CLEANING AND ORGANIZING DATA--

ridership.py:
    Run in order to combine and clean all of the data present in the various bicycle counter datasets. This takes a minute or two to run, since there are tens of thousands of rows in each of the nine datasets to process. It saves the final, combined dataset aggregated by year to pickle and CSV files.

existing_inf.py:
    Run in order to clean the existing bicycle infrastructure data in the "Existing Bike Facilities" CSV file. This returns the dataset broken down into streets, with start/end street intersections specified for each segment of bike infrastructure (important for networkx later). It is saved to pickle and CSV files.

--2: RIDERSHIP ANALYSIS--

ridership_graphing.py:
    Run in order to plot the percent change in amount of bike riders recorded at both the various bike counters around Seattle and in total. The resulting plot is saved as "annual_ridership.png".

--3: LENGTH ANALYSIS--

length.py:
    Run in order to generate a plot of total bike infrastructure network length (in miles) over time. The resulting plot is saved as "length_plot.png".

--4: NETWORK ANALYSIS--

bike_network.py:
    Run in order to plot the percent change in the "Connectivity Metric" of Seattle's bike infrastructure over time. This is calculated and plotted for both each individual kind of bike infrastructure and for the overall system. This uses the 'networkx' module. The resulting plot is saved as "connectivity_graph.png".

    The individual calculations for the Connectivity Metric for each kind of bike infrastructure, along with their percent changes, are saved to "connectivity_csv.csv" and "connectivity.pickle". The first six columns in the CSV file are the Connectivity Metric itself, whereas the following columns are the percent changes.






newAnalysis.py:

about the line graph:
This file contains all of the code from Exisiting_Bike_Facilities to make a line plot that shows the num of bike infrastructures built between 2010-2021. These years are chosen because it has data from the past 10 years and it would be reliable to use years that are recent to get an accurate and precise graph. The line plot has a legend on the top right-hand corner to allow the user to understand the different bike infrastructures and the lines that are being graphed. The plot is graphed in an up and down line because it represents the number of bike infrastructures built during the year, the line going down means that few or no bike infrastructures were being built. While the line going up means that more bike infrastructures were being built. We tried to sum up the number of bike infrastructures being built through the years 2010-2021, but we ran into a problem of not being able to work with the dataset since it contains data that cannot be groupby by the number of bike infrastructures and sum it. This is a messy dataset that requires filters and new columns to be added. We felt that the line going up and down shows a more accurate visualization of the number of bike infrastructure building progress.

about the line graph code:
To produce the line graph, we first read in the CSV file using pandas and parsed the CSV by the INSTALL_DATE. The INSTALL_DATE is when the bike infrastructure was first built. We then made another column to keep track of the number of the different bike infrastructures in the years, so that we can use the number later to produce the number of bike infrastructures being built between 2010-2021. Once we have a new column made for the number of bike infrastructures, we use groupby to sum the number of bike infrastructures. After we filter the data frame based on the years that we want 2010-2021. Finally, we plot the graph based on the INSTALL_DATE and NUM (the number of bike infrastructures) and categorize it based on CATEGORY (different bike infrastructures). The line plot is saved in a file called bike_infrastructures_plot.

about the map:

The second part of the file contains code to map the different bike infrastructures being built over the past 2 years between 2010-2021. We did the past 2 years because the results of the past 4 years show the same bike infrastructures from the past and there aren't any differences. When we did between 2012-2014, there are quite a few different bike infrastructures being built during this time, when we try to compare it from 2011-to 2014, the bike infrastructures are similar to 2010. This tells us that there wasn't any change in the number of bike infrastructures. This goes for the same between 2015-2018 and 2019-2021, these graphs represent the number of bike infrastructures built between these times.

about the map code:

For the map code we use data from the Planned_Bike_Facilities, then the Existing_Bike_Facilities dataset because the Planned_Bike_Facilities allows us to create graphs with its shape file. Also, the Planned_Bike_Facilities are data from the supported development of short and long-term use bike infrastructures in the Great Seattle Area. We first read the file using geopandas.read file(). We plotted the data frame without filtering to use as a base for plotting the different bike infrastructures throughout the year. This is a method that is similar to A5, where we colored the WA_data grey so that we can fill in the rest of the states. For each year, we filter the column INSTALL_DA by the date of the year that we wanted. INSTALL_DA is the data where the bike infrastructure was first built. For the plots where we wanted to filter it between 2012-2014, we manually have to set the data frame == to the year that we wanted. This is because we ran into a problem where the dates are strings. After we plot all of the graphs onto one file to allow the user to get an overview of the different bike infrastructures being throughout the years.
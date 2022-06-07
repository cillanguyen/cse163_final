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

-- 1: Cleaning and organizing data --

Line graph:
    To produce the line graph, we first read in the csv file using pandas and parsing the csv by the INSTALL_DATE. The INSTALL_DATE is when the bike infrastructure was first built. We then made another column to keep track of the number of the different bike infrastructures in the years, that we can use the number later to produce the number of bike infrastructures being built between 2010-2021. Once we have a new column made for the number of bike infrastructures, we use groupby to sum the number of bike infrastructures. After we filter the dataframe based on the years that we want 2010-2021.

Map graph:
    For the map code we use data from the Planned_Bike_Facilities, then the Existing_Bike_Facilities dataset because the Planned_Bike_Facilities allows us to create graphs with it's .shp file. Also the Planned_Bike_Facilities are data from the supported development of short and long term use bike infrastructures in the Great Seattle Area. We firsted read in the file using geopandas.readfile(). We plotted the dataframe without filtering to use as a based for plotting the different bike infrastructures throughout the year. This is a method that is similar to A5, where we colored the WA_data grey that we can fill in the rest of the states. For each year, we filter the column INSTALL_DA by the date of the year that we wanted. INSTALL_DA is the data where the bike infrastructure was first built. For the plots where we wanted to filter it between 2012-2014, we manual have to set the dataframe == to the year that we wanted. This is because we ran into a problem where the dates are strings.

-- 2: Producing the plot --

Line graph:
    Finally we plot the graph based on the INSTALL_DATE and NUM (the number of bike infrastructures),and categorize it based on CATEGORY (different bike infrastructures). The line plot is saved in a file called bike_infrastructures_plot.

Map graph:
    While filtering the INSTALL_DAT based on the selected years, use fig, ax to plot the graph onto one png file. This will allow the user to examine all four graphs at once. After plotting, four graphs should be produced.


create_csv.py
This file is used to create a series of csv files related to the number of different bike infrastructures, years and the number of riders in each districts.
These new datasets would be stored in a directory called 'DISTRICT' and would be used later in the prediction.py to be combined with the number of riders in each districts corresponding to years.


prediction.py:
--1: Create new datasets which consistes of bike infrastructures and number of riderships and do machine learning training.
--2: Train the new dataset by using the random forest regressor model.
    The new datasets are named based on different districts.
    The results are displayed by bar plots.
    All the new datasets and plots are stored in the directory 'Feature_Result'.
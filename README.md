# sqlalchemy-challenge

## Project Aim

This project learns the use of SQLalchemy, part of python SQL toolkit to access, manage and analyse data in sqlite file source using python scripts. 

## Project Description

This project is divided into 2 sections:

First part of project would be utilising Jupyter notebook and importing python SQL libraries, matplotlib, and pandas to explore climate data. 
2 CSV files would be used to for data exploration and analysis.

Second part of project is to utlise flask from python library to design climate web page.  
This is to design a Flask API based on the queries developed. Database is given as SQlite file. 

### Benefits of SQLalchemy
 - It provides a common interface for all type of database
 - Using python codes can generate more complex analysis
 - Enable to import substantial libraries to carry out different types of data modelling
 
### Disadvantages of SQLalchemy
- Intense code script needed
- Can be non-user friendly when dealing with complex analysis
- Many errors could occur from identation, capital letters and more
- Could be more time-intensive than other SQL app when dealing quick data analysis

## Project Method

### First section: Analyse and explore climate data

#### First analysis: Precipitation analysis
    - Create connections using python sqlachemy library such as create_engine, automap_base, and Session to connect to hawaii.sqlite database provided
    - Tables extracted from database named as measurement
    - From measurement table, extract precipitation data as 'prcp', and date data as 'date'
    - Obtain latest date of the data and extract one year back of precipitation data
    - Do not input date as parameter variable. Date needs to be input as following format: "%Y-%m-%d" when specify in the filter query. 
    - There will be more than one rainfall values in each date, as it specified the data taken for different stations
    - The extracted one year precipitation data then converted to pandas dataframe
    - Dataframe is then being cleaned by removing NA values, and also sort the data by dates in increasing order.
    - Type of data is also being checked, especially date is changed to "datetime" data type
    - Importing matplotlib library to plot data with x-axis being date, and y-axis being precipitation in millimetre values
    - X-ticks frequency needs to be reduced as x-ticks are too substantial and packed
    - This data is plot using line graph, not bar graph

#### Second analysis: Statin analysis
    - Tables extracted from database named as station
    - From station table, extract date data as 'date', station name as "station"
    - Need to determine total count of the each stations, need to use "func.count" in the filter query as opposed to "count()" that gives one distinct value
    - For loop is then used to extract total count for each stations
    - Then, need to determine temperature values for most active station;
    - This is done by joining 2 tables, matching their common values which is "station" name and find the corresponding temperature values under "tobs"
    - Within same filter query, "func.avg", "func.min", "func.max" are input into the queries to calculate the minimum, maximum and average temperature values. 
    - Same method, queries are appended to input date range for 1 year, in the format: "%Y-%m-%d", to extract temperature data. 
    - Using Matplotlib library, plot histogram with bins=12 (across 12 months), and x-axis being temperature

### Second section: Design climate app
    - First need to install: pip install flask
    - Create connections using python sqlachemy library such as create_engine, automap_base, and Session to connect to hawaii.sqlite database provided
    - First make "/" route: To start the homepage, and list all the available routes.
    - Second make "/api/v1.0/precipitation" route: Develope query that returns date as key, and precipitation as value in list dictionary
    - Third make "/api/v1.0/stations" route: To return all data from dataset
    - Fourth make "/api/v1.0/tobs" route: In combination from analysis result found from above precipitation analysis, 
       query for only most active station,and returns its one year most recent temperature data
       
    - Fifth make "/api/v1.0/<start>" route. This is imparting user input date value in this format: "%Y-%m-%d" within <start> of the url.
     Query will return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
     Input date value by user is responded within def(start) of the script that links with URL. 
     As no end date specified, it is by default the script would run through the final date of the data. 
     Hence date filter would be equal or bigger than input date value by user. 
     
     - Sixth make "/api/v1.0/<start>/<end>" route. This is imparting user input starting date value within <start>,
     and ending date value within <end> of the url with date format: "%Y-%m-%d". Input date values by user is responded within def(start, end) of the script that links with URL.
     Since date range is specified for user, hence date filter would be bigger than starting date, but smaller than ending date.
     
     - The results for all queries made need to be appended into empty dictionary first then empty list using for loop so final output could turned into json file. 
     - Then all data would be displayed in webpage as Json format by using "jsonify" function
     
     
     - To run python script with flask, make sure terminal is in dev/base environment by typing "conda activate dev"
     - Direct terminal to the path where the written script is store
     - Then run the file type "python app.py" (or any other given file name.py)
     - Click on the route link provided by : "ctrl+click"
     - When webpage opens: copy the link directory provided and connect with the base URL. 
     
## References
   - How to Change the DateТime Tick Frequency for Matplotlib.(31/12/2021).Data Plot Plus Python. Retrieved on 08/05/2023, from: <https://dataplotplus.com/change-datetime-tick-label-frequency-matplotlib-plots/>
   - Fixing common date annoyances(2021). Matplotlib. Retrieved on 08/05/2023, from: <https://matplotlib.org/3.3.4/gallery/recipes/common_date_problems.html>
   - Module 10: Advanced SQL Course Material. (2023). Monash Univerisity- Data Analytics Online Bootcamp. Retrieved on 1/5/2023
     
    



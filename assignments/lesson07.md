# Assignment 7 — Pandas Part II: Data cleaning and wrangling

Complete the tasks below. Please turn in a single Jupyter notebook named `7_first_last.ipynb` (substitute your first and
last name). Please run Kernel > Restart & Run All on your notebook before turning in.

## The Deutsche Bahn Departures dataset

For this assignment, we will use Pandas to examine the 
[GTFS (General Transit Feed Specification)](https://gtfs.de) for all the high-speed trains (ICEs only) from 
Deutsche Bahn for a typical day. The dataset has already been downloaded
and pre-summarized for you, and can be loaded from the file `../data/deutsche_bahn_departures_20250923.tsv`.

### A. Reading and summarizing

1. Import the tab-separated values file `deutsche_bahn_departures_20250923.tsv` as a DataFrame called `df` with default 
   data types, with the first row as column labels (columns) and the first columns as row labels (indexes).
2. The indexes should be the trip IDs (representing one train), but with individual stops for each of the trains.
   How many **different trips** are in this DataFrame? How many metadata columns?
3. What is the earliest departure on the dataset? What is the latest?
4. What is the average and standard deviation of the stop layover (difference between arrival and departure times, 
   in minutes)? What is the shortest stop? What is the longest?

### B. Indexing, slicing, and writing

1. Make a new DataFrame called `df_stuttgart`. Can you filter out all the trains that pass through Stuttgart?
2. Are you able to improve the filters and figure out how many trains are actually departing from Stuttgart?
3. You want to leave from Stuttgart Hbf after lunch and want to find a fitting train that goes to 
   Frankfurt. Find at least one alternative on the dataset, save it as a DataFrame called `df_str_fra`, and write the 
   route to a file.

### C. Merging, joining, and concatenating

1. After the previous exercises, you drank one coffee in Frankfurt and admired the big buildings, but not it's time to 
   go back. Find one connection back to Stuttgart, and assume at least one hour has passed since the previous arrival
   time from `df_str_fra`. Save this DataFrame as `df_fra_str`.
2. Concatenate the two DataFrames `df_str_fra` and `df_fra_str` using the `concat()` function.
3. Create a new DataFrame called `df_stops` that should contain the properties of the stops in the dataset (columns 
   `stop_id`, `stop_name`, `stop_lat`, `stop_lon`) dropping all duplicates.
4. Drop the columns `stop_name`, `stop_lat`, `stop_lon` from the `df_str_fra`. Join `df_stops` with `df_str_fra` 
   using the `join()` function and store the result as `df_joined`.
5. Do the same as in the previous exercise, but this time use the `merge()` function. Store the result as `df_merged`.

### D. Applying functions

1. Make a new dataframe called `df_trips` with all the individual trips from the entire dataset containing only 
   the **start and end locations of the trip**.
2. Make a new dataframe called `df_segments`, containing the different segments of the trips. Each rows consists of the
   departure location, the arrival location, and the departure and arrival times.
3. For the `df_segments`, calculate all the segment lengths (in minutes). Which one is the longest? Which one is the
   shortest?

### E. Sorting

1. Sort the rows in `df_stops` by `stop_name` values from A to Z and store the result on the same DataFrame
   (Hint: you can use `inplace=True`.)
2. Sort the rows in `df_stops` by latitude and longitude. What is the station that is the furthest north in Germany?

## **Bonus Assignment:** Clean the data yourself

The GTFS has been downloaded and pre-summarized for you and contains only partially what is available on the original
dataset. The full data can be found on the folder `../data/deutsche_bahn_long_distance_rail/`.

Your goal is to figure out how to put the data together. You already know what the final dataset should look like. Here
are the constraints used on the original dataset:

- `route_short_name` should start with `"ICE "`
- `agency_name` should start with `"DB"`
- route `start_date` and `end_date` should contain the date `20250923`, which is a **Tuesday**.
- We do not forget to exclude trips that were canceled on that specific day.
- We select the columns `trip_id`, `stop_sequence`, `route_short_name`, `arrival_time`, `departure_time`, `stop_name`,
  `stop_lat`, `stop_lon`.

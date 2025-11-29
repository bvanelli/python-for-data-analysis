# Assignment 09 — Pandas Part III: Group operations

## A. World Series Winners Analysis

The file `../data/WorldSeriesWinners.txt` contains a list of World Series winners from 1903, one year of event per line.

1. Load the data from `WorldSeriesWinners.txt` into a pandas' DataFrame with appropriate columns. Make sure to include 
   the year in the `Year` column.
2. Add a column called `Decade` that represents which decade each win occurred in (1900, 1910, 1920, 1930, etc.).
3. Using `groupby()`, calculate:
   - The total number of World Series wins per team.
   - The total number of World Series wins per decade and team.
4. Create a table showing teams (rows) vs decades (columns) with the count of wins in each cell, using the 
   `groupby()` result from item 3. The table will look like:

| Team             | 1910 | ... |
|------------------|------|-----|
| Boston Americans | 1    | ... |
| Chicago Cubs     | 2    | ... |

## B. Foreigner data multi-level Aggregation

Using the foreigners dataset `../data/12521-0008-foreigners_germany_until_2019.csv` from our class:

1. Transform the `Date` column into a datetime type and extract the year from it as a number.
2. Create a table with:
   - Index: `Origin`.
   - Columns: `Year` and `Residence permit`.
   - Values: `Count` (sum of both gender columns).
3. Using `groupby()` with multiple columns, calculate:
   - The total number of foreigners per type of residence permit for each year.
   - The average number of foreigners per origin across all years.
4. Find the top 5 residence permit types for all years (use data from the **latest year** for the ranking).
5. Create a new DataFrame showing year-over-year growth for the top 5 residence permits.
   **Hint**: Use `pct_change()` on the pivoted data.

## **Bonus Assignment**: Employment Sector Evolution

Load our dataset `../data/employment-12211-9008_en.csv` into a pandas' DataFrame. We are interested in 
calculating the gender gap percentage per sector over time. Create a "growth rate" analysis showing which sectors 
grew fastest for each gender. Choose three different sectors and plot their growth rates.

**Hint:** You can analyse growth rates using `pct_change()` for percentage or `diff()` for absolute difference. You
can decide on which approach you want to take.

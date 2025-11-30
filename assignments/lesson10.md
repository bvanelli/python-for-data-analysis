# Assignment 10 — Statistics Packages

For this assignment, we will use daily climate data from Zugspitze (1950–2024), downloaded from the Deutscher
Wetterdienst (German Weather Service). The data file is available in the repository at
`../data/zugspitze_klima_tag_19500101_20241231_05792.txt`.

## Set up and explore the dataset

1. Load the data and use `describe()` to get basic statistics for all numeric columns.
2. Calculate and print the following statistics for "Snow depth daily value (cm)":
    - Mean and standard deviation
    - Minimum and maximum values
    - 25th, 50th (median), and 75th percentiles
3. Find the date with the highest snow depth.

## Time series aggregation and regression

1. Using the entire dataset, aggregate the "Snow depth daily value (cm)" by year and plot the result using 
   `sns.regplot` with `order=1`. What do you observe?
2. Subselect the data for a specific year of your choice. Group the data by weekly values and create a column called
   "WEEK" that shows the corresponding week number. Calculate the mean value for "Snow depth daily value (cm)" for all
   weeks in that year.
3. Use Seaborn's `sns.regplot()` with `order=1` to create a linear regression plot for item 2. Was the fit
   good enough?
4. Increase the order of the polynomial regression until your model fits the data from item 2 well.
5. Use numpy to extract the parameters of the best-fitting polynomial model from item 4, then apply the model
   to a different year. Could your model predict the snow depth in that year, or was it off?
6. Reselect data for 5 consecutive years and group the data by monthly average values and try to fit a polynomial model
   to the data.
7. Fit a sine wave to the data from item 6.

## Correlation analysis

1. Evaluate the correlation between the following pairs of variables. For each pair, calculate the Pearson 
   correlation coefficient using `scipy.stats.pearsonr()`:
    - The "Daily average temperature (C)" vs "Snow depth daily value (cm)".
    - The "Sunshine duration daily total (hours)" vs "Snow depth daily value (cm)".
    - The "Daily mean relative humidity (%)" vs "Snow depth daily value (cm)".
2. Create scatter plots with regression lines for each pair using `sns.regplot()`. Use a 1x3 subplot layout.
3. Based on your correlation coefficients and the plots, which pair shows the strongest correlation?

## Outlier detection and distribution analysis

1. Using the yearly averaged "Snow depth daily value (cm)" data create a probability plot using `scipy.stats.probplot()`
   to check if the snow values follow a normal distribution.
2. Calculate the Z-score for all yearly snow depth values using `scipy.stats.zscore()`.
3. Identify outlier years using the Z-score method with a threshold of |Z-score| > 1.96 (95% confidence level). Print
   the years and their corresponding snow depth. They should represent years with an extreme amount of snow.

## **Bonus Assignment**: Temperature heatmap visualization

Create a new column called "Season" based on the month:

- Winter: December, January and February.
- Spring: March, April and May.
- Summer: June, July and August.
- Fall: September, October and November.

Draw a Seaborn [heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) of the data to visualize 
temperature patterns across years and seasons. Use a color palette like 
[coolwarm](https://seaborn.pydata.org/tutorial/color_palettes.html#other-diverging-palettes) to display results.

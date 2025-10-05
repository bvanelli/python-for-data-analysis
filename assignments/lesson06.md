# Assignment 06 — Pandas Part I: Basic operations

## A. Loading data

The Wikipedia page for the data for [States of Germany](https://en.wikipedia.org/wiki/States_of_Germany) was downloaded
and placed inside the `../data/States of Germany - Wikipedia.html`. You can open the file: it is an exact copy of the
original Wikipedia page (at the time of export).

Our goal today is to explore pandas data loading, and we are interested in the table from the dataset called 
_States > List_ that contains a table listing all States and general information like population and GDP.

1. Load the table on pandas (**Hint**: familiarize yourself with the 
   [`pandas.read_html()`](https://pandas.pydata.org/docs/reference/api/pandas.read_html.html) function.
   You might need to install a package, that you already know how to do).
2. Print the first and last three entries of the DataFrame.
3. Display the index and columns of the dataset.

## B. Transforming the metadata

1. Some column names still contain the Wikipedia references (i.e., `[6]`). Clean up the column names with appropriate
   names.
2. Get `describe()` the statistics for the _Population_ column?
3. Get the `info()` for the dataset.
4. Set the first column of the dataset (state name) as the index.

## C. Finding and replacing data

Based on the preview of the DataFrame, you can see that some columns have improper values. Fix the following:

1. The _Capital_ column has missing entries (i.e., `–`). Find those entries with `.iloc` and replace them.
2. The _Since_ column contain reference tags (i.e., `[10]`). Find those entries with `.loc` and replace them.
3. The _Since_ is still shown as object. Convert this column to a proper pandas timestamp column.
4. Inspect the resulting `dtypes`. Check if all the data loaded correctly and fix any columns with incorrect data type.

## D. Exporting the data

1. Export your cleaned-up table in the CSV format. Open the file to check if everything is there.
2. Export your cleaned-up table in the Excel format. Open the file to check if everything is there.

## **Bonus Assignment:** Data manipulation

You probably noticed that the page contains more than one table when using the `read_html` function. One of them is
the _Unincorporated areas in German states_ table that contains data about areas that are not part of any municipality
(i.e., forest and mountain areas).

Load this table and create a new column on your previous dataset with the most up-to-update number of 
_Unincorporated areas_ (area is missing on the dataset). 

After you are done, use the `info()` to get information about your new column.

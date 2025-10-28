# Assignment 05 — Numpy, Pandas, and Matplotlib introduction

## A. NumPy Foundations

1. Generate and explore an array:

- Create a 1D array of 20 random floating-point numbers between 0 and 1.
- Compute and print its mean, standard deviation, and sum.
- Reshape this array into a 4x5 array and print its new shape, as well as the array itself.

2. Understanding NumPy efficiency and flexibility:

- Create a NumPy array of integers from 0 to 100 (inclusive).
- Extract all elements divisible by both 2 and 5 using NumPy boolean masks and conditional slicing. Print the result.
- Explicitly explain why this approach is faster than using Python lists and looping.

3. Many data science workflows involve generating data. Simulate the following scenarios:

- Generate 1000 random numbers following a normal (Gaussian) distribution with a mean of 10 and a standard
  deviation of 2. Plot a histogram of the numbers using Matplotlib.
- Create a diagonal 5x5 matrix where the diagonal contains evenly spaced numbers between 1 and 10. Print the matrix.

## B. Pandas for Structured Data

1. Explore a dataset:

- Load the `employment-12211-9008_en.csv` file into a Pandas DataFrame.
- Print the first 5 rows and the column names of the dataset to understand its structure.
- Identify the total number of rows that belong to the "Education" sector.
- For the dataset, choose a year and calculate the percentage of jobs in "Education" in relation to
  the total number of jobs.

## C. Matplotlib for Visualization

- Choose a year from the dataset. Create side-by-side bar charts to compare the male and female employment for each 
  area of work.

## **Bonus Assignment:** Stacked Chart Comparison

Create a [stacked chart](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html) to represent 
the total number of jobs in each category for each year.

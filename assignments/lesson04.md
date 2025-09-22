# Assignment 4 — Taking Input, Reading and Writing Files, Functions

Complete the tasks below. You should turn in a single Jupyter notebook named `3_first_last.ipynb` (substitute your first
and last name); please run Kernel > Restart & Run All on your notebook before turning in. Also, turn in the input CSV
file used in question B3. For questions where Python scripts are used instead of the Jupyter notebook (questions A1, B1,
B2), instructions are provided about pasting output/scripts into Markdown cells in your notebook.

## A. Taking input, reading and writing files, functions

1. Write some code, without using functions, that calculates the average of 5 numbers. Do it three different ways:

- Write a .py file that takes input from the command line using `input()`. After the script works, paste the text of
  the file into your Jupyter notebook.
- Write a .py file that takes input from the command line using `argv`. After the script works, paste the text of
  the file into your Jupyter notebook.
- Enter code into two Jupyter notebooks cells: the first stores value as variables, and the second computes the
  average.

2. Using functions, write some code that takes two strings, prints them with the first letter capitalized, prints them
   with all letters capitalized, prints the first and last letter of each, prints the length of each, and then prints
   the concatenation of the two strings. Do it two different ways:

- Write a .py file that uses `argv`. After the script works, paste the text of the file into your Jupyter notebook.
- In your Jupyter notebook, comment out the `argv` portions and hard code in the values of your strings. Then make
  sure the code runs the same.

3. Using a text editor, create a comma-separated values (CSV) file with 5 columns and 5 rows. Save it in the same
   directory as your Jupyter notebook. In the Jupyter notebook, read and print the file in different ways, and write new
   files, as follows:

- Read your CSV file using `read()`, `readline()`, or `readlines()`, and print the output to the screen (`print()`
  command is optional in notebooks!).
- Do the same but use a `with` block and a different one of `read()`, `readline()`, or `readlines()`.
- Using either of the two above methods to read in the file, then change one row of data (i.e., modify the string or
  list), then write your csv data to a new file.
- Read your CSV file using Pandas and display the resulting DataFrame.
- Save your DataFrame to a new file using Pandas.

## **Bonus Assignment:** Recursion

A recursive function is a function that calls itself. Previously in [lesson 2](lesson02.md), we have implemented
the Fibonacci sequence using a for loop. Write a recursive function that takes as input the number `n` 
calculates n-th number of the Fibonacci sequence.

**Tip:** the n-th number of the Fibonacci sequence is the sum of the two previous numbers, n-1-th and n-2-th.

# Assignment 4 — Taking Input, Reading and Writing Files, Functions

## A. Taking input, reading and writing files, functions

1. Write some code, without using functions, that calculates the average of 5 numbers. Do it three different ways:

- Write a .py file that takes input from the command line using `input()`. After the script works, paste the text of
  the file into your Jupyter notebook.
- Write a .py file that takes input from the command line using `argv`. After the script works, paste the text of
  the file into your Jupyter notebook.
- Enter code into two Jupyter notebook cells: the first stores value as variables, and the second computes the
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

- Read your CSV file using `read()`, `readline()`, or `readlines()`, and print the output to the screen (the `print()`
  command is optional in notebooks).
- Do the same but use a `with` block and a different one of `read()`, `readline()`, or `readlines()`.
- Using either of the two above methods to read in the file, then change one row of data (i.e., modify the string or
  list), then write your csv data to a new file.

## B. Reading and writing files with the standard library

1. Using the `csv` module, read in the CSV file you created in the previous question. Print the data to the screen.
2. Using the `csv` module, write a new CSV file with the same data as the original, but with the header columns 
   as uppercase. Is this file any different from the original?

## C. Functions for file handling

1. Write a function, using the standard CSV library, that reads a CSV file and returns a list of dictionaries. Each
   element on the list will represent a row on the CSV file, and the keys for the dictionaries will be the column
   headers. Run your function against the following CSV file:

```csv
name,gender,age
Max Mustermann,male,27
Erika Mustermann,female,23
```

You should get the following output:

```json
[
    {
      "name": "Max Mustermann",
      "gender": "male",
      "age": "27"
    },
    {
      "name": "Erika Mustermann",
      "gender": "female",
      "age": "23"
    }
]
```


## **Bonus Assignment:** Recursion

A recursive function is a function that calls itself. Previously in [lesson 2](lesson02.md), we implemented
the Fibonacci sequence using a for loop. Write a recursive function that takes as input the number `n` 
and calculates the n-th number of the Fibonacci sequence.

**Tip:** the n-th number of the Fibonacci sequence is the sum of the two previous numbers, n-1-th and n-2-th.

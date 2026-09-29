---
title: CES Python Programming - Fundamentals (2,5 ECTS)
author: Brunno Vanelli
geometry: margin=2.5cm
---

## Overview

An introduction to data science using Python and Pandas with Jupyter notebooks. Software covered:

- Python 3
- IPython environment and Jupyter notebooks

Course topics include:

- Fundamentals of Python and its data types
- Python programming logic, conditionals, loops, functions, and Python objects
- Data analysis packages NumPy and Pandas
- Plotting packages like Matplotlib
- Basic statistics
- Modules and classes
- Concepts of clean code
- AI-assisted programming

## Instructor

- Brunno Vanelli
- Email: [brunno.vanelli@hs-albsig.de](mailto:brunno.vanelli@hs-albsig.de)
- Pages: [GitHub](https://github.com/bvanelli) · [LinkedIn](https://www.linkedin.com/in/bvanelli/)

## Organization of classes

There are a total of 15 double classes. The material for each class consists of:

- One double-class going over the lesson material using some live examples on Jupyter Notebooks.
- One assignment for self-study.
- For some classes, an optional bonus assignment (if you want to learn things more in depth).
- Additional reading material for the class content (from the textbook, online resources, etc.)

## Grading

The grade will be based on a final project that exercises the concepts learned in the class. The final project is split
into two parts, and each one of them will exercise your problem-solving skills in a data-science task. Both parts are
done in groups of two students and will consist of the delivery of a notebook describing how exactly you solved the
problem.

You will be graded on:

- The explanations of the decisions you made for each task.
- The thought process behind each decision: why was each decision made?
- The consistency of your results, and whether you can explain them in a few sentences.
- Is your notebook well-formatted and easy to read? Is it well-organized?

## Module description

### 1. Class overview: Python, IPython, Packages, and Jupyter Notebooks

- Introduction to the course, basic information, introduction to the "notebook-style" exercises, and assignments
- Introduction to materials: online resources, textbooks, guidelines for usage of AI tools
- Quick run-through of what Python is with live-demo
- Launching a Jupyter Notebook
- Basics of Python syntax, variables, and data types
- All slides, exercises, and assignments will be on the Git repository
- **Assignment:** setting up a Github account and forking the class repository **(recommended)**. The content can also
  be downloaded directly without account creation. Afterward, you are invited to run through the exercises on your own.

### 2. Printing, Strings, Numbers

- Working and formatting strings
- String interpolation with format and fstrings
- Numbers and math
- Describing functions
- Getting help on libraries and functions
- Documenting functions with docstrings

### 3. Logic, Loops, Syntax, and data types

- Logic: boolean operations, equality testing
- Loops: for, while, break, continue, if else statements
- Range, increment, more complex loops
- More data types: List, tuples, dictionaries, sets, datetime, NoneTypes.

### 4. Taking Input, Reading and Writing Files, Functions

- Taking input from the user: either with Python scripts or in the notebook
- Structuring a notebook file
- Short description documenting the notebook with markdown syntax
- Reading and writing basic files
- Defining functions

### 5. NumPy, Pandas and Matplotlib introduction

- Basic random functions, arrays, NumPy arrays
- Basic NumPy arrays, generating arrays from Python objects, array generating functions, array indexing, and linear
  algebra
- Basic Pandas dataframes, loading data from files, basic column operations
- Basic matplotlib, basic data selection, and plotting

### 6. Pandas Part I: Series, files, and indexing

- Pandas Series datatype
- DataFrame operations: index, columns
- dtypes, info, describe, head, tail
- More complex file operations: read_csv, to_csv, read_excel, to_excel
- Indexing with bracket/dot notation, loc, iloc
- transpose

### 7. Pandas Part II: Data cleaning and wrangling

- Basic data cleaning and preparation
- Data wrangling: join, combine reshape
- Pandas functions map, filtering, indexing, sorting
- Removing null values - dropping data, ffill, bfill

### 8. Plotting with matplotlib

- Using the API for basic plots
- Legends, labels, plot types, line types
- Multiple plots in the same figure
- Working with axis and different kinds of plots (bars, scatter, etc.)
- Introduction to 3D plotting

### 9. Pandas Part III: Group operations

- How to transform dataframes based on what you want to achieve: Group by, Pivot table, melt, stack, crosstab

### 10. Statistics Packages

- Mean, median, and percentiles
- Regression (polyfitting. and outliers)
- Independence test
- Variance calculation and outlier detection
- Clustering with scikit-learn

### Recap. Case-study for Airport data

- Cleaning and joining multiple real datasets for airport data
- Data aggregation and summarization
- Data analysis and plotting of interesting metrics

### 11. Basic forecasting: Prophet models

- Pandas timeseries: Converting to and from datetime objects
- Periods and resampling
- Timezone handling
- Windowing, smoothing, rolling averages
- Basic time series analysis and forecasting with Prophet.

### 12. Modules and classes

- What is object-oriented programming (OOP)?
- Importing modules and using classes
- Basic inheritance and polymorphism
- Implementing dataclasses as data transfer objects (DTOs)
- Why do we test? What is test-driven development? Introduction to code testing: pytest
- Basic package organization

### 13. Concepts of clean coding

- PEP8, coverage, formatting, type system, linters, documentation, and best practices.
- Development in a team environment: feature workflows and communication with the team.

### 14. AI-assisted development

- What are LLMs actually doing: what are their limitations?
- Common pitfalls of AI development: context length, hallucinations
- How to develop with coding assistants called Agents: building a data processing pipeline using only AI agents
- What is Model Context Protocol (MCP) and tool usage, and how it has changed AI automations.

## Bibliography

- [_Learn Python 3 the Hard Way_, by Zed Shaw](https://learnpythonthehardway.org/python3/)
- [_Python for Data Analysis_, by Wes McKinney](https://wesmckinney.com/book/)

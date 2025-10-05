# Assignment 02 — Printing, Strings, Numbers

## A. Python basics, strings, printing (Shaw Exercises 1–10)

1. Take the file of Python code you generated in Exercise 1, called `ex1.py`, and run it on the command line. Copy the
   command and output from your terminal and paste it in a Markdown cell in your Jupyter notebook. (Ex1)
2. Print a sentence that contains a phrase in double quotes; print a sentence that contains an apostrophe. (Ex1)
3. Deliberately enter five incorrect commands (in separate cells) and interpret the error messages (in Markdown
   cells). (Ex1)
4. Add comments to your code in \#2 and \#3 explaining what is happening. (Ex2)
5. Write and evaluate five mathematical expressions. (Ex3)
6. Assign values to three numeric and three string variables. (Ex4)
7. Print values of the six variables you assigned in \#6. (Ex4–5)
8. Concatenate two strings into a third string, then find the length of all three strings. 
9. Print the three strings from \#9 with a tab between the first and second and a newline between the second and third.
10. Print the three strings from \#9 with a stored formatter. (Ch7–8)
11. Print a piece of text with five lines using both newline characters and a text block. (Ex9)
12. Print a string containing a backslash, single-quote, double-quote, newline, and tab. (Ex10)

## B. Implementing the Fibonacci Sequence

The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous 
two numbers in the sequence. The sequence looks like this:

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

1. Create a new notebook file and name it "fibonacci"
2. Create variables for the first two Fibonacci numbers (0 and 1)
3. Print these two numbers
4. Add comments explaining what Fibonacci numbers are
5. Create a loop that runs n - 2 times (we already have 2 numbers)
6. Calculate the next number (sum of previous two)
7. Print each new number

### C: Putting It All Together

1. Combine all previous steps into one function by creating a function called "fibonacci" that takes the starting 
numbers `n1` and `n2`, as well as the number of numbers `m` to print.
2. Test with different inputs (try n1 = 1, n2 = 5, m = 10)

Example output:

```python
fibonacci(0, 1, 5)
0
1
1
2
3
5
```

## **Bonus Assignment:** GCD (Greatest Common Divisor)

The GCD of two numbers is the largest positive integer that perfectly divides both numbers.
For example, GCD of 48 and 60 is 12, while the GDC of 10 and 7 is 1.

1. Create a function called "find_gcd" that takes two numbers as input and outputs the GCD of those two numbers.
2. Test with different inputs (try pairs like 48,60 or 54,24 or 10,7)

Example output:

```python
find_gcd(48, 60)
12
```

**Tip:** for this assignment, you might need to look into the *boolean comparison*.
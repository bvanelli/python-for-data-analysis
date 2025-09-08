# Lesson 02 — Printing, Strings, Functions, Numbers

## Fibonacci Sequence Assignment

The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous 
two numbers in the sequence. The sequence looks like this:

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

### Part 1: Understanding Basics

1. Create a new notebook file and name it "fibonacci"
2. Write a function that prints "Hello World" to test your setup
3. Run the program to make sure everything works

### Part 2: First Two Numbers

1. Create variables for the first two Fibonacci numbers (0 and 1)
2. Print these two numbers
3. Add comments explaining what Fibonacci numbers are
4. Test your program

### Part 4: Building the Sequence

1. Create a loop that runs n - 2 times (we already have 2 numbers)
2. Calculate the next number (sum of previous two)
3. Print each new number

### Part 5: Putting It All Together

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

## Bonus Assignment: GCD (Greatest Common Divisor)

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
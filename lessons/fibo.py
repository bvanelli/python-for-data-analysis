"""
This file is here as it is referenced in lesson 12.
"""


def fib(n: int):
    """
    Write Fibonacci series up to a max value of n
    """
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    print()


def fib2(n: int):
    """
    Return Fibonacci series up to a max value of n
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))

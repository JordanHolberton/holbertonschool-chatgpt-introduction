#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n by 1 in each iteration
    return result

# Check if an argument is provided
if len(sys.argv) > 1:
    try:
        # Convert the argument to an integer
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Please provide a valid integer as an argument.")
else:
    print("Usage: ./factorial.py <number>")

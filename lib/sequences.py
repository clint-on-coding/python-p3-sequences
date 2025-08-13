#!/usr/bin/env python3

def print_fibonacci(length):
    # Handle edge cases
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return

    # Start with first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Build the sequence up to the desired length
    while len(fib_sequence) < length:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    # Print the result
    print(fib_sequence)


# This runs only when you execute this file directly
if __name__ == "__main__":
    print_fibonacci(9)

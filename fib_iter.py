def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Generate Fibonacci sequence up to n terms
n_terms = 10
print(f"Fibonacci sequence: {fibonacci_iterative(n_terms)}")

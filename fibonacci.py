# Function to generate Fibonacci series up to n terms
def fibonacci_series(n):
    series = []
    a, b = 0, 1
    while len(series) < n:
        series.append(a)
        a, b = b, a + b
    return series

# Number of terms
n_terms = 10

# Generate Fibonacci series
fib_series = fibonacci_series(n_terms)

# Print the Fibonacci series
print(f"Fibonacci series up to {n_terms} terms:")
print(fib_series)

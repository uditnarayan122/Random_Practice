def squares_list(n):
    return [x ** 2 for x in range(n)]

# Create a list of squares of numbers from 0 to n-1
n = 5
print(f"List of squares up to {n-1}: {squares_list(n)}")

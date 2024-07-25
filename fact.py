def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Find the factorial of a number
number = 5
print(f"Factorial of {number}: {factorial(number)}")

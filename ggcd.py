def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Find the GCD of two numbers
a, b = 48, 18
print(f"GCD of {a} and {b}: {gcd(a, b)}")

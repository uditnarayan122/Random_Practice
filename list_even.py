def generate_even_numbers(n):
    return [x for x in range(n) if x % 2 == 0]

# Generate a list of even numbers up to n
n = 20
print(f"Even numbers up to {n}: {generate_even_numbers(n)}")

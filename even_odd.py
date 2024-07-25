def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

# Check if a number is even or odd
number = 15
print(f"{number} is even: {is_even(number)}")
print(f"{number} is odd: {is_odd(number)}")

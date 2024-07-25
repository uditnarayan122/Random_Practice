import random

def generate_random_list(size, start, end):
    return [random.randint(start, end) for _ in range(size)]

# Generate a list of random numbers
size = 10
start = 1
end = 100
print(f"Random list: {generate_random_list(size, start, end)}")

import random
import statistics

# Function to generate a list of random numbers
def generate_random_numbers(count, start, end):
    return [random.randint(start, end) for _ in range(count)]

# Number of random numbers to generate
n_numbers = 20

# Range of random numbers (inclusive)
range_start = 1
range_end = 100

# Generate random numbers
random_numbers = generate_random_numbers(n_numbers, range_start, range_end)

# Sort the random numbers
sorted_numbers = sorted(random_numbers)

# Calculate mean and median
mean = statistics.mean(sorted_numbers)
median = statistics.median(sorted_numbers)

# Print the results
print("Generated Random Numbers:")
print(random_numbers)
print("\nSorted Random Numbers:")
print(sorted_numbers)
print(f"\nMean of the numbers: {mean}")
print(f"Median of the numbers: {median}")

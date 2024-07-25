def average(lst):
    return sum(lst) / len(lst) if lst else 0

# Calculate the average of a list
numbers = [10, 20, 30, 40, 50]
print(f"Average of the list: {average(numbers)}")

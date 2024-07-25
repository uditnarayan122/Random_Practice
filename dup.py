def remove_duplicates(lst):
    return list(set(lst))

# Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
print(f"List without duplicates: {remove_duplicates(numbers)}")

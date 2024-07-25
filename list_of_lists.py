def flatten(lst):
    return [item for sublist in lst for item in sublist]

# Flatten a list of lists
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(f"Flattened list: {flatten(list_of_lists)}")

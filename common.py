def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(f"Common elements: {common_elements(list1, list2)}")

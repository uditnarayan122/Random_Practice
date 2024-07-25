from collections import Counter

def count_frequency(lst):
    return Counter(lst)

# Count the frequency of elements in a list
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Element frequency: {count_frequency(lst)}")

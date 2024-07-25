def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1])

# Sort a list of tuples by the second element
tuples = [(1, 'c'), (2, 'a'), (3, 'b')]
print(f"Sorted tuples: {sort_tuples(tuples)}")

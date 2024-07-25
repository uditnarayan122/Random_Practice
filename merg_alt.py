def merge_alternately(list1, list2):
    return [elem for pair in zip(list1, list2) for elem in pair] + list1[len(list2):] + list2[len(list1):]

# Merge two lists alternately
list1 = [1, 3, 5]
list2 = [2, 4, 6, 8, 10]
print(f"Merged list: {merge_alternately(list1, list2)}")

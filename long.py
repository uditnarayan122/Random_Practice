def longest_word(words):
    return max(words, key=len)

# Find the longest word in a list
words = ["apple", "banana", "cherry", "date"]
print(f"Longest word: {longest_word(words)}")

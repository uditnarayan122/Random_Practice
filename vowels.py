def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

# Count the number of vowels in a string
string = "Hello, World!"
print(f"Number of vowels in '{string}': {count_vowels(string)}")

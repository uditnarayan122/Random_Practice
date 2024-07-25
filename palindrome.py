def is_palindrome(s):
    return s == s[::-1]

# Check if a string is a palindrome
string = "racecar"
print(f"Is '{string}' a palindrome? {is_palindrome(string)}")

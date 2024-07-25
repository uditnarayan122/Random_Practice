import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Check if a string is a valid email address
email = "test@example.com"
print(f"Is '{email}' a valid email? {is_valid_email(email)}")

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Generate a random password of a given length
password_length = 12
print(f"Random password: {generate_password(password_length)}")

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# Convert a decimal number to binary
decimal_number = 42
print(f"Binary representation of {decimal_number}: {decimal_to_binary(decimal_number)}")

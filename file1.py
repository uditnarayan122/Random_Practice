# Function to read the contents of a file and return it as a string
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to count the number of words in a string
def count_words(text):
    words = text.split()
    return len(words)

# Function to write the word count to a file
def write_word_count(file_path, word_count):
    with open(file_path, 'w') as file:
        file.write(f"Word count: {word_count}")

# Path to the input file
input_file_path = 'input.txt'

# Path to the output file
output_file_path = 'output.txt'

# Read the contents of the input file
text = read_file(input_file_path)

# Count the number of words in the text
word_count = count_words(text)

# Write the word count to the output file
write_word_count(output_file_path, word_count)

print(f"The word count has been written to {output_file_path}.")

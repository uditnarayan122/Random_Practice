def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

# Transpose a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Transposed matrix: {transpose_matrix(matrix)}")

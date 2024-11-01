"""
    Simple python package to multiply two given matrices
"""


# Function to multiply two matrices
def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """Multiply two given matrices in python

    Args:
        A (list[list[int]]): first metrix
        B (list[list[int]]): second metrix

    Raises:
        ValueError: if metrices cannot be multiplied

    Returns:
        list[list[int]]: resulting metrix
    """

    # Get the dimensions of the matrices
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError(
            "Number of columns in A must be equal to number of rows in B")

    # Initialize the result matrix with zeros
    result = [
        [0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


if __name__ == "__main__":
    # Example matrices
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    B = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    # Multiply the matrices
    result = matrix_multiply(A, B)

    # Print the result
    for row in result:
        print(row)

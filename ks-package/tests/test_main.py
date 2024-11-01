import pytest
from ks_package.main import matrix_multiply


def test_matrix_multiply():
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

    expected_result = [
        [30, 24, 18],
        [84, 69, 54],
        [138, 114, 90]
    ]

    result = matrix_multiply(A, B)
    assert result == expected_result


def test_matrix_multiply_invalid_dimensions():
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    B = [
        [1, 2],
        [3, 4]
    ]

    with pytest.raises(ValueError, match="Number of columns in A must be equal to number of rows in B"):
        matrix_multiply(A, B)


if __name__ == "__main__":
    pytest.main()

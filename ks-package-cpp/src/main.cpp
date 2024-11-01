#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <stdexcept>
// #include <iostream>

using namespace std;

/* Multiply the given matrices
Args:
    A: Matrix A.
    B: Matrix B.

Returns:
    result matrix
*/
vector<vector<int>> multiply_matrices(const vector<vector<int>>& A, const vector<vector<int>>& B) {
    int rowsA = A.size();
    int colsA = A[0].size();
    int rowsB = B.size();
    int colsB = B[0].size();

    if (colsA != rowsB) {
        throw invalid_argument("Number of columns in A must be equal to number of rows in B");
    }

    vector<vector<int>> result(rowsA, vector<int>(colsB, 0));

    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            for (int k = 0; k < colsA; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}


PYBIND11_MODULE(ks_package_cpp, m) {
    m.def("multiply_matrices", &multiply_matrices, 
    "A function that multiplies two matrices\n\n"
    "Args:\n"
    "   A(list[list[int]]): Matrix A.\n"
    "   B(list[list[int]]): Matrix B.\n"
    "Returns:\n"
    "   list[list[int]]: Result matrix.");
}

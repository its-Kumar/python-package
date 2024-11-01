#include <Python.h>

#include <stdlib.h>

// A function to multiply two matrices of size m x n and n x p
static PyObject * multiply_matrices(PyObject * self, PyObject * args) {
    PyObject * listA, * listB;
    int m, n, p;

    if (!PyArg_ParseTuple(args, "iiO!iiO!", & m, & n, & PyList_Type, & listA, & n, & p, & PyList_Type, & listB)) {
        return NULL;
    }

    // Allocate memory for the matrices and the result matrix in one go
    int * A = (int * ) malloc(m * n * sizeof(int));
    int * B = (int * ) malloc(n * p * sizeof(int));
    int * result = (int * ) calloc(m * p, sizeof(int));

    // Initialize matrix A
    for (int i = 0; i < m; i++) {
        PyObject * sublistA = PyList_GetItem(listA, i);
        for (int j = 0; j < n; j++) {
            A[i * n + j] = PyLong_AsLong(PyList_GetItem(sublistA, j));
        }
    }

    // Initialize matrix B
    for (int i = 0; i < n; i++) {
        PyObject * sublistB = PyList_GetItem(listB, i);
        for (int j = 0; j < p; j++) {
            B[i * p + j] = PyLong_AsLong(PyList_GetItem(sublistB, j));
        }
    }

    // Perform matrix multiplication
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            for (int k = 0; k < n; k++) {
                result[i * p + j] += A[i * n + k] * B[k * p + j];
            }
        }
    }

    // Create a Python list to return the result matrix
    PyObject * resultList = PyList_New(m);
    for (int i = 0; i < m; i++) {
        PyObject * sublist = PyList_New(p);
        for (int j = 0; j < p; j++) {
            PyList_SetItem(sublist, j, PyLong_FromLong(result[i * p + j])); // Corrected indexing
        }
        PyList_SetItem(resultList, i, sublist);
    }

    // Free allocated memory
    free(A);
    free(B);
    free(result);

    return resultList;
}

// Method definitions
static PyMethodDef KSMethods[] = {
    {
        "multiply_matrices",
        multiply_matrices,
        METH_VARARGS,
        "Multiply two matrices of size m x n and n x p."
    },
    {
        NULL,
        NULL,
        0,
        NULL
    }
};

// Module definition
static struct PyModuleDef ksmodule = {
    PyModuleDef_HEAD_INIT,
    "ks_package_c",
    NULL,
    -1,
    KSMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_ks_package_c(void) {
    return PyModule_Create( & ksmodule);
}

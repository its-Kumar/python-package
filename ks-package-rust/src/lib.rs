use pyo3::prelude::*;
use pyo3::wrap_pyfunction;


/// Multiply two matrices of size m x n and n x p. 
/// 
/// Args: 
/// a (List[List[int]]): Matrix A 
/// b (List[List[int]]): Matrix B 
/// 
/// Returns:
/// List[List[int]]: The resulting matrix after multiplication
#[pyfunction]
#[pyo3(text_signature = "(A: list[list[int]], B: list[list[int]])")]
fn multiply_matrices(a: Vec<Vec<i16>>, b: Vec<Vec<i16>>) -> PyResult<Vec<Vec<i16>>> {
    let rows_a = a.len();
    let cols_a = a[0].len();
    let rows_b = b.len();
    let cols_b = b[0].len();

    if cols_a != rows_b {
        return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
            "Number of columns in A must be equal to number of rows in B",
        ));
    }

    let mut result = vec![vec![0; cols_b]; rows_a];

    for i in 0..rows_a {
        for j in 0..cols_b {
            for k in 0..cols_a {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    Ok(result)
}

#[pymodule]
fn ks_package_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(multiply_matrices, m)?)?;
    Ok(())
}

import time

import ks_package
import ks_package_c as ks
import ks_package_cpp as kp
import ks_package_rust as ksr


def run_module(func, *args):
    start = time.time()
    res = func(*args)
    print(res)
    end = time.time()
    return end - start


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

c_time = run_module(ks.multiply_matrices, 3, 3, A, 3, 3, B)
print(f"C Module run time:  {c_time * 1000:.6f} ms")

cpp_time = run_module(kp.multiply_matrices, A, B)

print(f"C++ Module run time: {cpp_time * 1000:.6f} ms")

rst_time = run_module(ksr.multiply_matrices, A, B)
print(f"Rust Module run time:  {rst_time * 1000:.6f} ms")

py_time = run_module(ks_package.matrix_multiply, A, B)
print(f"Python Module run time:  {py_time * 1000:.6f} ms")

from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="ks_package_rust",
    version="0.1.0",
    rust_extensions=[
        RustExtension(
            "ks_package_rust.ks_package_rust",
            "Cargo.toml",
         binding="pyo3")],
    packages=["ks_package_rust"],
    zip_safe=False,
)

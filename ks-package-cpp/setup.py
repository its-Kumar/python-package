import pybind11
from setuptools import Extension, setup

ext_modules = [
    Extension(
        'ks_package_cpp',  # This should match the module name you want to import
        ['src/main.cpp'],
        include_dirs=[pybind11.get_include()],
        language='c++'
    ),
]

setup(
    name='ks_package_cpp',
    version='0.1',
    ext_modules=ext_modules,
)

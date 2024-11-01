# Python Package

Create Python packages/modules with using different languages such as Python, C, C++, and Rust.

## Python Libraries
### In Python
Create python modules written in python

#### Folder Structure
```sh
ks-package              # package root dir
├── README.md
├── dist                # for distributing the package
│   ├── ks_package-0.1.0-py3-none-any.whl
│   └── ks_package-0.1.0.tar.gz
├── ks_package          # src dir
│   ├── __init__.py
│   └── main.py         # source code for package
├── pyproject.toml      # package metadata and dependencies
└── tests               # test cases for the package
    ├── __init__.py
    └── test_main.py
```

#### Build
Create package easily with `poetry`

    poetry new <package_name>

Build

    poetry build

Install

    poetry install
    <or>
    pip install dist/<package_name>-0.1.0-py3-none-any.whl

### In C++
#### Folder Structure
```sh
ks-package-cpp/
├── README.md
├── build
├── dist                # for distribution
│   └── ks_package_cpp-0.1-cp311-cp311-linux_x86_64.whl
├── ks_package_cpp
│   └── __init__.py
├── pyproject.toml
├── setup.py            # required `setup.py` file
├── src
│   └── main.cpp
└── tests               # test cases
    ├── __init__.py
    └── test_main.py
```

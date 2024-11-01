from setuptools import Extension, setup

ext_modules = [
    Extension(
        'ks_package_c',  # Module name
        sources=['src/main.c'],  # C source file
    ),
]

setup(
    name='ks_package_c',
    version='0.1',
    description='A simple example package using C',
    ext_modules=ext_modules,
)

import setuptools
from distutils.core import setup, Extension

setup(name="hash_module", version='1.0',
      ext_modules=[Extension('hash_module',
                             ['hash.c'])])

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    setuptools.setup(
        name='group_1',
        packages=setuptools.find_packages(),
        version='0.0.1',
        long_description=long_description,
        description='User reg/login',
        author='group_1',
        license='MIT',
        package_dir={},
        install_requires=['sys', 'time'],
        test_suite='tests',
        python_requires=">=3.6",
    )

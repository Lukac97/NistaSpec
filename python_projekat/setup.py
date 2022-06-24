from distutils.core import setup, Extension

setup(name="hash_module", version='1.0', ext_modules=[Extension('hash_module',
                                                         ['hash.c'])])
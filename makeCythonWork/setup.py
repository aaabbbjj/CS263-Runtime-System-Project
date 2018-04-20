from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'This is app name',
  ext_modules = cythonize("functionFile.pyx"),
)
from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Measure cython performance with OOP',
  ext_modules = cythonize("cythonDefinition.pyx"),
)
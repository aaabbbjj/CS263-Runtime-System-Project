from cythonDefinition import *
import time

def compute_nonCython(a, b, N):
    s = 0
    for j in range(100000):
        s += 1
    for i in range(N):
        s += (a * a + i * b)
    return s

def compute_python_withCythonClass(f, a, b, N):
    s = 0
    for j in range(100000):
        s += 1
    for i in range(N):
        s += f.compute(a) + i * b
    return s

def compute_python_withCythonClass2(f, a, b, N):
    s = 0
    for j in range(100000):
        s += 1
    for i in range(N):
        s += f.compute(a, b, i)
    return s

def compute_python_withCythonClass3(f, a, b, N):
    s = 0
    for j in range(100000):
        s += 1
    s += f.compute(a, b, N)
    return s

class PythonFunctionClass(CythonInterface):
    def compute(self, x):
        return x * x

class PythonFunctionClass2(CythonInterface2):
    def compute(self, a, b, i):
        return a * a + b * i

# Measure elapsed time without Cython 
stamp0 = time.time()
compute_nonCython(1.5, 1.6, 300000)
stamp1 = time.time()
print("Elapsed time without Cython: %f" % (stamp1 - stamp0))

# Measure elapsed time with Cython
# python function, Cython class
stamp0 = time.time()
compute_python_withCythonClass(CythonFunctionClass(), 1.5, 1.6, 300000)
stamp1 = time.time()
print("Elapsed time with Cython, python function, Cython class: %f" % (stamp1 - stamp0))

# Measure elapsed time with Cython
# python function, python class
stamp0 = time.time()
compute_python_withCythonClass(PythonFunctionClass(), 1.5, 1.6, 300000)
stamp1 = time.time()
print("Elapsed time with Cython, python function, python class: %f" % (stamp1 - stamp0))

# Measure elapsed time with Cython
# cython function
stamp0 = time.time()
compute_cython_withCythonClass(CythonFunctionClass(), 1.5, 1.6, 300000)
stamp1 = time.time()
print("Elapsed time with Cython, Cython function, Cython class: %f" % (stamp1 - stamp0))

print("--------")

# Measure elapsed time with Cython
# python function, Cython class
stamp0 = time.time()
compute_python_withCythonClass2(CythonFunctionClass2(), 1.5, 1.6, 300000)
stamp1 = time.time()
print("Elapsed time with Cython, python function, Cython class: %f" % (stamp1 - stamp0))

# Measure elapsed time with Cython
# python function, python class
stamp0 = time.time()
compute_python_withCythonClass2(PythonFunctionClass2(), 1.5, 1.6, 300000)
stamp1 = time.time()
print("Elapsed time with Cython, python function, python class: %f" % (stamp1 - stamp0))

# Measure elapsed time with Cython
# cython function
stamp0 = time.time()
compute_cython_withCythonClass2(CythonFunctionClass2(), 1.5, 1.6, 300000)
stamp1 = time.time()
print("Elapsed time with Cython, Cython function, Cython class: %f" % (stamp1 - stamp0))

print("--------")
# Measure elapsed time with Cython
# python function, python class, different function
stamp0 = time.time()
compute_python_withCythonClass3(CythonFunctionClass3(), 1.5, 1.6, 300000)
stamp1 = time.time()
print("Elapsed time with Cython, python function, python class: %f" % (stamp1 - stamp0))
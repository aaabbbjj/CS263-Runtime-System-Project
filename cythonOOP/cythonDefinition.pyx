cdef class CythonInterface:
    cpdef double compute(self, double x) except *:
        return 0

cdef class CythonInterface2:
    cpdef double compute(self, double a, double b, int i) except *:
        return 0

cdef class CythonInterface3:
    cpdef double compute(self, double a, double b, int N) except *:
        return 0

cdef class CythonFunctionClass(CythonInterface):
    cpdef double compute(self, double x) except *:
        return x * x

cdef class CythonFunctionClass2(CythonInterface2):
    cpdef double compute(self, double a, double b, int i) except *:
        return a * a + b * i

cdef class CythonFunctionClass3(CythonInterface3):
    cpdef double compute(self, double a, double b, int N) except *:
        cdef double s
        cdef int i
        s = 0
        for i in range(N):
            s += a * a + b * i
        return s

def compute_cython_withCythonClass(CythonInterface f, double a, double b, int N):
    cdef int i
    cdef int j
    cdef double s
    s = 0
    for j in range(100000):
        s += 1
    for i in range(N):
        s += f.compute(a) + i * b
    return s

def compute_cython_withCythonClass2(CythonInterface2 f, double a, double b, int N):
    cdef int i
    cdef int j
    cdef double s
    s = 0
    for j in range(100000):
        s += 1
    for i in range(N):
        s += f.compute(a, b, i)
    return s
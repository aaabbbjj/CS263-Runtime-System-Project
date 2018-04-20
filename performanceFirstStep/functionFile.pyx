def compute_nonType(a, b, N):
    s = 0
    for i in range(N):
        s += (a * a + i * b)
    return s

def compute_type(double a, double b, int N):
    cdef int i
    cdef double s
    s = 0
    for i in range(N):
        s += (a * a + i * b)
    return s
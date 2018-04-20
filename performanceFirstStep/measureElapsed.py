from functionFile import *
import time

def compute_nonCython(a, b, N):
    s = 0
    for i in range(N):
        s += (a * a + i * b)
    return s

# measure elapsed time without Cython
stamp0 = time.time()
compute_nonCython(1.2, 1.3, 9000)
stamp1 = time.time()
print("Elapsed time without Cython: %f" % (stamp1 - stamp0))

# measure elapsed time with Cython, without type
stamp0 = time.time()
compute_nonType (1.2, 1.3, 9000)
stamp1 = time.time()
print("Elapsed time with Cython, no type: %f" % (stamp1 - stamp0))

# measure elapsed time with Cython, with type
stamp0 = time.time()
compute_type(1.2, 1.3, 9000)
stamp1 = time.time()
print("Elapsed time with Cython, with type: %f" % (stamp1 - stamp0))

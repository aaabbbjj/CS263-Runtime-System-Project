## What does Cython do
Cython is a Python compiler. One could write python function, use Cython to compile them to C codes, and when one call this function, it could be faster with the improved performance given by C.  

Cython could be easily downloaded with pip:
```
pip3 install Cython
```

## Make Cython work
1. Write a setup.py
2. Write a python function and store it in a file ended with pyx, such as functionFile.pyx
3. Run:
```
python3 setup.py build_ext --inplace
```
4. This will generate a funtionFile.c file, which is further complied to a .so (shared object) file. An .o file is under the directory "build".
5. Then one could call this function in python, like in callPythonFunction.py

## Performance first step
We start with two functions compiling with Cython
1. compute_nonType is a function without type definition
2. compute_type is a function with type definition
With type definition, the for-loop in compute_type could be compiled to pure C code, with further improved performance.  
  
The program shows this result:  
Elapsed time without Cython: 0.000941  
Elapsed time with Cython, no type: 0.000690  
Elapsed time with Cython, with type: 0.000019  
  
Which suggests that even though Cython could improve performance, with type definition, the performance could be improved much further. 



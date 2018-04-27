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

## Performance first step with Cython
We start with two functions compiling with Cython
1. compute_nonType is a function without type definition
2. compute_type is a function with type definition
With type definition, the for-loop in compute_type could be compiled to pure C code, with further improved performance.  
  
The program shows this result:  
Elapsed time without Cython: 0.000941  
Elapsed time with Cython, no type: 0.000690  
Elapsed time with Cython, with type: 0.000019  
  
Which suggests that even though Cython could improve performance, with type definition, the performance could be improved much further. 

## OOP with Cython
Tried to use "interface" defined in Cython to improve performance of python class
Firstly Build a cython class called "CythonInterface". Then we have two options for inheritance:
1. write a Cython class on this interface.
2. write a python class on this interface.
Then we have three options to use this function:
1. write a Cython function with Cython class as argument
2. write a python function with Cython class as argument
3. write a python function with python class as argument 
  
The program shows this result with CythonInterface:  
Elapsed time without Cython: 0.038080
Elapsed time with Cython, python function, Cython class: 0.056352
Elapsed time with Cython, python function, python class: 0.073154
Elapsed time with Cython, Cython function, Cython class: 0.002014
  
Apparently, using Cython interface does not improve performance. Only Cython function improves performance. Then we change function, and with CythonInterface 2, we get:
Elapsed time with Cython, python function, Cython class: 0.051460
Elapsed time with Cython, python function, python class: 0.074996
Elapsed time with Cython, Cython function, Cython class: 0.002762

Using Cython function still does not improve performance. Maybe because calling a Cython function has some overhead. So we should avoid calling Cython function in each for-loop, and put for-loop in Cython function. We tried this method. And weith CythonInterface3, we get:
Elapsed time with Cython, python function, python class: 0.006195

Based on the above results, we come to a conclusion that python using Cython class could improve performance only if the overhead is not too much. For instance, if we keep calling a Cython class to do 
simple computation, it may be slower than pure python codes. Because the overall overhead do more harm 
than the improvement given by Cython.




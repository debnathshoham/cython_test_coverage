# cython: language_level=3, linetrace=True, lineprofile=True

cimport cython

cpdef int add_test_cython(int a , int b):
    return a+b

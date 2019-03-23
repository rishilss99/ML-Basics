"""Important and can be used in ML"""
import numpy as np

new_dtype = np.dtype([('Name',np.unicode,16),('Grade',np.float64,(2,))])
array1 = np.array([('Sarah',(8,7)),('John',(5,7))],dtype=new_dtype)

print(array1)
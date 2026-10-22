"""accessing array"""

import numpy as np

arr=np.array([10,20,30,40])
arr2=np.array([[1,2,3,4],[9,7,6,5]])
print(arr)
print(arr2)
"""indexing"""
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr2[0][3])
print(arr2[1][2])
"""slicing"""
print(arr[0:1])
print(arr[0:2])
print(arr[0:4])
print(arr2[0][0:4])
print(arr2[0][2:4])
print(arr2[1][0:4])

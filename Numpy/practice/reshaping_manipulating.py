# reshape()

import numpy as np

arr=np.array([10,20,30,40,5,6])

# reshape=arr.reshape(2,3)
# print(reshape)
# print(arr)

##############################################################

"""flattern"""
# .ravel()-> return view
# .flattern()-> copy

arr2=np.array([
    [1,2,3],[4,3,2]
])

print(arr2.ravel())
print(arr2.flatten())


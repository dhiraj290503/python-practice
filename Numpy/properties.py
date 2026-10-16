## shape
## size
## type


"""Shape"""

import numpy as np

# arr=np.array([
#     [1,2,3],
#     [4,5,6],
#     [6,7,8]
# ])

# print(arr)
# print("shape of array=>",arr.shape)

###########################################################################

"""size"""
# arr=np.array([
#     [1,2,3],
#     [4,5,6],
#     [6,7,8]
# ])

# print(arr)
# print("total no. of elements in array=>",arr.size)

"""ndim"""
# to check number of dimension


arr=np.array([
    [1,2,3],
    [4,5,6],
    [6,7,8]
])

arr2=np.array([
    [
        [1,2,3],
        [4,5,6],
        [6,7,8]
    ],
    [
        [6,7,8],
        [4,5,6],
        [1,2,3]
    ],
    [
        [9,8,7],
        [6,7,8],
        [2,4,6]
    ]
])

arr3=np.array([
    [
        [
            [1,2,3],
            [4,5,6]
        ]
    ],
    [
        [
            [4,5,6],
            [1,2,3]
        ]
    ]
])


# # print(arr)
print("no. of dimensions in array=>",arr.ndim)
# print("Shape of array=>",arr3.shape)
# print("total no. of elements in array=>",arr3.size)

############################################################################################
"""dtype"""
## to check the data type of array
# print(arr3.dtype)

############################################################################################

"""changing data type of array"""
# print(arr2.astype(str))
# print(arr2)
# print(arr2[0].astype(float))
# print((arr2[:3,:3].astype(float)))
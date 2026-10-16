import numpy as np

# list1=[1,2,3,4,5]
# print("List",list1)

# arr= np.array([6,7,8,9,1])
# print("Array",arr)

############################################################################

"""1D array"""
##
# arr=np.array([10,20,30,40,50,60])
# print("1D array=>",arr)

# arr2=np.array([
#     [1,2,3],
#     [4,5,6] 
# ])

# print("2D array=> \n",arr2)
############################################################################

"""multidimensional array / Matrix / """
# m=np.array([
#     [1,2,3],[4,5,6]
# ])

# print("matrix",m)
############################################################################

"""Array with default values"""
# arr=np.zeros(3)
# print(arr)

# arr=np.ones((2,3))
# print(arr)

# full(shape,value)
# arr=np.full((4,3),7)
# print(arr)

############################################################################ 
"""creating sequences of numbers in numpy"""
## arange(start,stop,step)

# arr = np.arange(2,11,2)
# print(arr)

############################################################################ 
"""creating identity matrix"""
## square matrix with 1 with diagonals and zeroes else where
## eye(size)

# im=np.eye(3)
# im=np.eye(4)
# im=np.eye(5)
# print(im)
############################################################################ 
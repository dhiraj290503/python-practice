
## np.insert(array,index,value,axis=none)
## array    -> original array
## index    -> position to insert value
## value    ->  data to be inserted
## axis     -> if it is none it is inserted into flattern array
## axis = 0 -> row
## axis = 1 -> column


import numpy as np

# arr=np.array([10,20,30,40])
# print(arr)

# new_arr=np.insert(arr,2,300)
# print("*"*80 )
# print(new_arr)

##################################################################################

"""inserting into 2D array"""

# arr=np.array([
#     [1,2,3],
#     [8,9,10]
# ])
# print(arr)
# #insert a new row at index 1
# new_arr=np.insert(arr,0,[100,200,300],axis=0)

# # insert a new column at index 1
# new_arr=np.insert(arr,1,[100,200],axis=1)

# #axis = None => flatent array
# # new_arr=np.insert(arr,1,[100,200,300],axis=None)

# print("*"*80 )
# print(new_arr)

##################################################################################

"""append"""

# arr=np.array([10,20,30,40,50,60])
# new_arr=np.append(arr,[700,800,900])
# print(arr)
# print("*"*80)
# print(new_arr)
##################################################################################

"""join / concatinate"""
## np.concatenate((arr1,arr2),axis=0)
## axis 0 = vertical stacking
## axis 1 = horizontal stacking

# arr=np.array([10,20,30])
# arr2=np.array([40,50,60])

# # new_arr=np.concatenate((arr,arr2))      # [10 20 30 40 50 60]
# # new_arr=np.concatenate((arr,arr2),axis=0) # [10 20 30 40 50 60]
# new_arr=np.concatenate((arr,arr2),axis=1) #  axis 1 is out of bounds for array of dimension 1
# print(new_arr)

##################################################################################

"""remove"""
# np.delete(arr,index,axis)

# arr=np.array([10,20,30,40])
# new_arr=np.delete(arr,3)
# print(arr)
# print(new_arr)

# arr=np.arange(6).reshape(2,3)
# arr=np.array([
#     [1,2,3],[4,5,6]
# ])
# print(arr)
# print("*"*80)
# # new_arr=np.delete(arr,0)
# new_arr=np.delete(arr,0,axis=0)
# # new_arr=np.delete(arr,0,axis=1)
# print(new_arr)

##########################################################################3

"""stacking"""
## vertically -> vstack()
## horizontally ->hstack()

# arr=np.array([1,2,3])
# arr2=np.array([4,5,6])

# # arr3=np.vstack((arr,arr2))
# arr3=np.hstack((arr,arr2))
# print(arr3)

"""spliting"""
## np.split
## np.hsplit
## np.vsplit

arr=np.array([10,20,30,40,50,60])

print(np.split(arr,3))
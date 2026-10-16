
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

arr=np.array([
    [1,2,3],
    [8,9,10]
])
print(arr)
#insert a new row at index 1
# new_arr=np.insert(arr,1,[100,200,300],axis=0)

# insert a new column at index 1
# new_arr=np.insert(arr,1,[100,200],axis=1)

#axis = None => flatent array
new_arr=np.insert(arr,1,[100,200,300],axis=None)

print("*"*80 )
print(new_arr)

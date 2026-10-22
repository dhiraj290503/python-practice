import numpy as np

## buitl in function
## 1 np.isnan => detect missing values
## 2 np.nan_to_num() => replace missing values with another number got from the np.nan
## 3 np.isinf() => to check wheather the values are infinite 

## => nan=not a number

# np.isnan(arr)

# arr=np.array([1,2,3,np.nan,5,np.nan,6])
# print(np.isnan(arr))

## np.nan_to_num(arr,nan=value)
# cleaned_arr=np.nan_to_num(arr,)
# cleaned_arr=np.nan_to_num(arr,nan=777)
# print(cleaned_arr)

## 3 np.isinf(arr)

arr=np.array([1,2,3,np.nan,5,np.nan,6,np.inf])
print(np.isinf(arr))

# to replace infinity values
clear_arr=np.nan_to_num(arr,posinf=10,neginf=-10)
print(clear_arr)

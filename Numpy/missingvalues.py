import numpy as np

## buitl in function
## 1 np.isnan => detect missing values
## 2 np.nan_to_num() => replace missing values with another number got from the np.nan
## 3 np.isinf() => to check wheather the values are infinite 

## => nan=not a number

# np.isnan(arr)

arr=np.array([1,2,3,np.nan,5,np.nan,6])
print(np.isnan(arr))
1.59.49
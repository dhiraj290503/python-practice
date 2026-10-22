import numpy as np
arr=np.array([10,20,30,40])

print(arr[arr > 25])
print(arr[arr < 25])
print(arr[(arr > 15) & (arr <35)])
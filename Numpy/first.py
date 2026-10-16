# temp=[31.2,31.8,35.1,36.6,39.1,40]
# total = 0

# for i in temp:
#     total+=i

# avg = total / len(temp)

# print(avg)
##################################################################################################

import numpy as np
temp=np.array([31.2,31.8,35.1,36.6,39.1,40])

avg = np.mean(temp)
print(avg)


"""Features of Numpy"""
## 50-100 times faster than python list
## use less memory
## supports easy maths operatiions
## used in AI, DS, DA

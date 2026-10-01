"""Dictinories"""
## mutable
## duplicate only values not keys
## key value pair
## follows the insertion order

# d={
#     "name":"Dhiraj",
#     "age":23,
#     "list1":[1,2,3,4,"Hello"],
#     "tuple":(1,2,3),
#     "set":{10,9,8}
# }

# print(d)
# print(d["name"])
# print(d["age"])
# print(d["list1"])

# d["dict1"]={1:10}
# print(d)

"""traversing"""

# for i in d:
#     print(i)
#     print(d[i])

# for i in d.values():
#     print(i)

# for i in d.keys():
#     print(i)

## 1 clear
## 2 copy
## 3 get

# a=[12,13,14,15]
# b=a

# b[0] = 120

# print(b)
# print(a)

# a=[12,13,14,15]
# b=a.copy()

# b[0] = 120

# print("a=>",a)
# print("b=>",b)

# d2= d.get("Dhiraj")

# print(d.items())


# dict1={
#     "name":"dhiraj"
# }

# dict2={
#     "age":23
# }

# for i in dict2:
#     dict1[i]=dict2[i]


# print(dict1)
# print(dict2)

# sum of values 
# d1={10:100,20:200,30:300}
# sum=0

# for i in d1:
#     sum+=d1[i]

# print(sum)

#frequency 

# a=[111,2,2,2,2,2,33,4,4,6,3,21,3,41,1,111,32,12,12,2,2]
# dict1={}
# for i in a:
#     if i in dict1.keys():
#         dict1[i]+=1
#     else:
#         dict1[i]=1


# print(dict1)

d1={10:100,20:200,30:300}

for i in d1:
    print(f"{d1[i]**2}")


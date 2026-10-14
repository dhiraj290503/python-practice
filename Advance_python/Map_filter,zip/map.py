"""Map"""
## map is used to apply a finction to multiple items
## tskes a list 
## applies the same function to every item of that list
## gives you back a new list (in python 3,it gives a map object which can convert to a list)
## udr map()

a=[1,2,3,4,5,6]

# result = map(lambda x:x*2,a)
# print(a)
# print(list(result))

def double(a):
    return a**2

result = map(double,a)

print(a)
print(list(result))
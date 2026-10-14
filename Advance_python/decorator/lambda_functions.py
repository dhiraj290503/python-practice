"""lambda function"""
## A lambda function is an anonymous function,inline function defined using the lambda keyword
## multiple arguments but only one 

# def add(a,b):
#     sum = a+b
#     return sum


# result=add(10,100)
# print(result)


# add = lambda a,b : a+b

# print(add(10,20))


add = lambda a:  f"hello even {a}" if a %2 ==0 else f"odd {a}"

print(add(1))
print(add(10))
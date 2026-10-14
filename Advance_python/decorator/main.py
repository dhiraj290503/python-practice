"""decorator"""
## it is just a function that modifies another function without changing its actual code
##  

# def decorate(func):
#     def wrapper(a,b):
#         print("Addition of given numbers !!")
#         func(a,b)
#         print("thankyou")
#     return wrapper
    


# @decorate
# def addition(a,b):
#     print(f"total is {a+b}")

# addition(12,12)



def decorate(func):
    def wrapper(*args,**kwargs):
        print("Addition of given numbers !!")
        func(*args,**kwargs)
        print("thankyou")
    return wrapper
    


@decorate
def addition(*args,**kwargs):
    total = sum(args) + sum(kwargs.values())
    print(f"total is {total}")

addition(12,12,24,52,a=10) 
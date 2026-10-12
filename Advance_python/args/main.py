"""Args and kwargs"""
## used in function definition to accept a flexible number of parameters.
## *args are used for multiple positional arguments and 
## **kwargs are used for multiple key word arguments 
## *args becomes tuple
## **kwargs becomes dictionary


# def fun(*args,**kwargs):
#     print("args: ",args)
#     print("kwargs: ",kwargs)


# fun(1,2,3, name="Adhraj",age=24)

# def addition(*args):
#     sum=0
#     for i in args:
#         sum = sum+i

#     print(sum)

# addition(10,20,30,40)


# def addition(**kwargs):
#    print(kwargs)
   

# addition(a=10,b=20,c=30,d=50)

def info(**krs):
    print("YOUR INFO IS: ")
    for i in krs:
        print(f"{i} : {krs[i]}")


info(name="sonya",age=24,add="pune")
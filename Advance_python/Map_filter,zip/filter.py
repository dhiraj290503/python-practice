"""FILTER"""
## as the name suggest is used to filter out the sutff
## takes a list (or other sequence)
## checks each item using a function (a test)
## keeps only the item that passes the test

# def even(x):
#     if x % 2==0:
#         return True
#     else :
#         False



# a=[1,2,3,4,4,5,10,6,32,78,8,9,9]

# result = filter(even,a)
# print(a)
# print("even numbers",list(result))

a=[1,2,3,4,4,5,10,6,32,78,8,9,9]
even =  lambda a :True if a % 2==0 else False

result = filter(even,a) 
print(list(result))
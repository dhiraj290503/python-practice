# class addition():
#     def __init__(self,a,b):
#         print(a+b)

# obj = addition(10,20)

"""class creation"""
## class is a blueprint of object
## always start a class name with capital letter (not compulosry)
## two types of things inside a class
## 1. Attribute => Variables defined inside a class are attributes
## 2.Methods => functions defined inside a class are methods

class Factory:
    a = 12 #=> attribute

    def hello(self): #=> method
        print("hello")

    print("hello im getting initilized")

Factory()

####################################################################

print(Factory().a)
Factory().hello()
"""objects in python"""
## object is instance of class

class Factory:
    a = 12 #=> attribute

    def hello(self): #=> method
        print("hello")

    print("hello im getting initilized")

obj = Factory()

print(obj.a)
obj.hello()
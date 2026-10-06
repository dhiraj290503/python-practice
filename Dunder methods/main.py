"""Dunder methods"""
# Magic methods are special methods whose names start and end with double underscores, like __init__() and __str__().
# Because of the double underscores, they are also called dunder methods (short for "double underscore").


class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

    def __str__(self):
        # print("hwllo how are you")
        return f"hello how are you {self.name}"
    
    def __add__(self,other):
        sum=0
        for i in other:
            sum=sum+i.age

        return f"Your sum of ages are : {self.age + sum}"

obj=Animal("Lion",21)
obj2=Animal("Cat",12)
obj3=Animal("tiger",32)

print(obj+(obj2,obj3))

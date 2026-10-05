"""Polymorphism"""

"""method overriding"""

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"Hello {self.name}")

    

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age

#     def show(self):
#         print(f"hello {self.name},your age is {self.age}")

# animal1=Animal("lion")
# person1=Human("dhiraj",24)

# # animal1.show()
# person1.show()

"""Duck typing"""

class Animal:
    def show(self):
        print("hello")

class Human:
    def show(self):
        print("hii")


obj = Animal()
obj2=Human()

obj.show()
obj2.show()
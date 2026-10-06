"""Encapsulation"""
## Encapsulation ==> in capsul 
## It makes your code clean and easy to use
## It keeps data safe from being changed by mistake
## It gives control voer what others can access or change

# class Factory:
#     a ="pune"

#     def show(self):
#         print("Hello I am pune Factory")

# class Bhopal(Factory):
#     def show(self):
#         print(super().a)
#         super().show()

# obj = Bhopal()
# obj.show()

# **************************************************************************

## Protected attributes and methods (=> _)
## naming convection to tell developers 
# class Factory:
#     _a ="pune"

#     def _show(self):
#         print("Hello I am pune Factory")

# class Bhopal(Factory):
#     def show(self):
#         print(super()._a)
#         super()._show()

# obj = Bhopal()

# obj.show()

"""Private attributes and methods"""
## it cannot be acceseed from outside the class -only from inside the class where it is defined
## in python we use two underscores(__) before the name to make it private

# class Factory:
#     __a ="pune"

#     def show(self):
#         print("Hello I am pune Factory")
#         print(Factory.__a)

# ## class Bhopal(Factory):
# ##     def show(self):
# ##         print(super().__a)
# ##         super().__show()

# obj = Factory()
# obj.show()

# 'super' object has no attribute '_Bhopal__a'


class Demo:
    def __init__(self): 
        self.name="Dhiraj"     #Public
        self._age = 24         #Protected
        self.__salary=100000   #private

    def show(self):
        print("Inside the class")
        print("Public",self.name)
        print("Protected",self._age)
        print("Private",self.__salary)

obj1 = Demo()
obj1.show()
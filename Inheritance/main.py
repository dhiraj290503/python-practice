# class Factory: #parent class /super class
#     a="im attribute mention inside factory"
#     def hello(self):
#         print("Im method mention inside factory")

# class FactoryPune(Factory): #child class/ sub classs
#     pass


# obj = Factory()

# """powers"""
# print(obj.a)

# obj2 = FactoryPune()
# print(obj2.hello())

"""constructor"""

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age
#     def show(self):
#             print(f"hello your name is {self.name} and age is {self.age}")
    

# # person1 = Human("john")
# # person1.show()

# animal1=Animal("lion")
# person1=Human("dhiraj",24)
# person1.show()
# animal1.show()


"""types of inheritance """
## 1.single Inheritance
## 2.Multiple Inheritance
## 3.Multilevel Inheritance

# class Animal:
#     AnimalName = "Lion"

# class Human:
#     HumanName="Dhiraj"

# class Robots(Animal,Human):  #multiple inheritance
#     RobotName="charli123"


# obj = Robots()
# print(obj.AnimalName)
# print(obj.HumanName)
# print(obj.RobotName)
######################################################################################

# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(selfname,age):
#         pass
    

# class Robots(Animal,Human):  #multiple inheritance
#     RobotName="charli123"


# obj = Robots()
############################################################################################
# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(selfname,age):
#         pass
    

# class Robots(Human,Animal):  #multiple inheritance
#     RobotName="charli123"


# obj = Robots()

"""3.Multilevel Inheritance"""
class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips


class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class Punefactory(BhopalFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets=pockets


obj = Punefactory()
"""Abstraction"""
## abstraction doesnot exist in python  but we can acheive it using a library
## it is used to simplify the  complex systems by focusing on essientisl features and hiding unncessary details


## Abstract classes and methods

from abc import ABC,abstractmethod

class abstract(ABC):
    @abstractmethod

    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass
    
        

class Square(abstract):
    def __init__(self,side):
        self.side=side
        
    def perimeter(self):
            print("created")

    def area(self):
            print("area created")


class Circle(abstract):
    def __init__(self,radius):
        self.radius=radius

    def perimeter(self):
        print("created")

    def area(self):
        print("area created")

circle1=Circle(7)
square1= Square(2)
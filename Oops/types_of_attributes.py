"""Types of attributes"""
## 1.class attributes
## 2.Instance attribute


"""class attributes"""
class Animal:
    name="lion"  #class attribute

    """Instance attribute"""
    def __init__(self,age):
        self.age=age #instance attribute


"""Types of methods"""
### 1.Instance Method
### 2.class method

class Animal:
    name="lion"

    def __init__(self,age):
        self.age=age

    def show(self): #Instance Method
        print("hello")

    @classmethod
    def hello(cls):
        print("how are you ")

    @staticmethod
    def static():
        print("Hello")


obj =Animal(12)

obj.show()
obj.hello()
obj.static()
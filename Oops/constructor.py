"""constructor"""


# class Factory:
#     a = 12 #=> attribute

#     def hello(self): #=> method
#         print("hello")

#     print("hello im getting initilized")

class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Your objects are {self.material},{self.zips},{self.pockets}")


reebok = Factory("leather",3,2)
campus= Factory("nylon",2,3)

# print(f"reebok pockets =>{reebok.pockets}")
# print(f"reebok pockets =>{campus.pockets}")

reebok.show()
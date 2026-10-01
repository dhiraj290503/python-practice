# a = int(input("enter a number: "))

# # a=0  

# print(10/a)
# # ZeroDivisionError: division by zero 
# print("division done")

################################################################################

"""except by exception name"""
# a = int(input("Enter a number: "))
# b = int(input("Enter a number to divide: "))

# try:
#     print(f"{a}/{b} = {a/b}")

# except ZeroDivisionError:
#     print("The given number canot be divided by zero")

# print("Division completed!!")

########################################################################################
"""except"""
# a = int(input("Enter a number: "))
# b = int(input("Enter a number to divide: "))

# try:
#     print(f"{a}/{b} = {a/b}")

# except Exception as e:
#     print(f"The given number canot be divided by zero got a {e} error")

# print("Division completed!!")

#########################################################################################
"""except"""
# a = input("Enter a number: ")
# # b = int(input("Enter a number to divide: "))

# try:
#     print(f"{10}/{a} = {10/a}")

# except Exception as e:
#     print(f"The given number canot be divided got a {e} error")

# print("Division completed!!")

######################################################################################################
"""Else"""
# a = int(input("Enter a number: "))
# b = int(input("Enter a number to divide: "))

# try:
#     print(f"{10}/{a} = {10/a}")

# except Exception as e:
#     print(f"The given number canot be divided got a {e} error")

# else:
#     print("Good there is no error")

# print("Division completed!!")

###################################################################################

"""Finally"""
# a = int(input("Enter a number: "))
# b = int(input("Enter a number to divide: "))

# try:
#     print(f"{a}/{b} = {a/b}")

# except Exception as e:
#     print(f"The given number canot be divided got a {e} error")

# else:
#     print("else => Good there is no error ")

# finally:
#     print("finally => I will run no matter what")

# print("Division completed!!")

######################################################################################

# age = int(input("Enter your age: "))

# if age < 10 or age>18:
#     raise ValueError("Your age must be between be between 10 and 18")

# else:
#     print("welcome to clube")

# print("the club will start soon")

######################################################################################
"""raise"""

age = int(input("Enter your age: "))
try:
    if age < 10 or age>18:
        raise ValueError("Your age must be between be between 10 and 18")

    else:
        print("welcome to clube")

except Exception as e:
    print(f"an error occur : {e}")

print("the club will start soon")
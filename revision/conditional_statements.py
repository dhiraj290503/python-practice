# a=int(input("enter a number: "))
# b=20

# if a == 5:
#     print("a == 5")
# elif a > 5 and a < 10 :
#     print(f"a==> {a}")
# elif a > 10 and a < 20:
#     print(f"{a} elif 2")
# else:
#     print(f"b=> {b}")

# 8888888***********************************************************************************

# a = int(input("enter first no: "))
# b = int(input("enter second no: "))

# if a > b:
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{b} is greater than {a}")

# 8888888***********************************************************************************

# gender = input("enter Gender(M/F): ")

# if gender == "M"  :
#     print("Good Morning sir")
# elif gender == "F":
#     print("Good Morning Madam")
# else:
#     print("enter a valid gender")

# 8888888***********************************************************************************

# a = int(input("Enter a Number: "))

# if a % 2 == 0:
#     print(f"{a} is even number")
# else:
#     print(f"{a} is odd number" )

# 8888888***********************************************************************************

# name=input("Enter your Name: ")
# age=int(input("Enter Your Age: "))

# if age >= 18:
#     print(f"congratulations {name} you are eligible to vote")
# else:
#     print("try next year")

# 8888888***********************************************************************************

# year=int(input("Enter a year: "))

# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

# 8888888***********************************************************************************

temp= int(input("enter temp in Celcius: "))

if temp < 0 :
    print("Freezing cold")
elif temp >=0 and temp < 10:
    print("very cold")
elif temp>=10 and temp< 20:
    print("cold")
elif temp >=20 and temp < 30:
    print("pleasant")
elif temp>=30 and temp < 40:
    print("Hot")
elif temp>=40:
    print("very hot")
else:
    print("enter a valid temp")
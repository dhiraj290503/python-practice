# a="dhiraj"

# for i in range(6):
#     print(a[i])

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# for i in range(1,11):
#     if i == 5:
#         break
#     
#     print(i)


# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)

"""for else"""

# for i in range(1,10):
#     if i==15:
#         print("break is executed")
#         break
#     print(i)

# else:
#     print("break is not executed")
# *********************************************************************************************************************

# n=int(input("enter a no: "))

# for i in range(n):
#     print("Hello World")


# *********************************************************************************************************************

# #naturL NOS UPTO N 
# n=int(input("enter a number: "))

# for i in range(1,n+1):
#     print(i)


# *********************************************************************************************************************
## reverse loop print n to 1
# n=int(input("Enter a no: "))

# for i in range(n,0,-1):
#     print(i)


# *********************************************************************************************************************

# #print a table of any number

# n= int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")


# *********************************************************************************************************************

## sum up to n terms

# n=int(input("enter a number: "))
# total=0

# for i in range(1,n+1):
#     total+=i
#     print(total)

# *********************************************************************************************************************

##factorial

# n=int(input("enter a number: "))
# fact=1

# for i in range(1,n+1):
#     fact*=i

# print(fact)

# *********************************************************************************************************************

## sum of all odd and even in range 
# n=int(input("enter a number: "))
# odd=0
# even=0

# for i in range(1,n+1):
#     print(i)
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i

# print("sum of even numbers =>",even)
# print("sum of odd numbers =>",odd)


# *********************************************************************************************************************

# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

# *********************************************************************************************************************

# num = int(input("Enter a number: "))

# total = 0

# for i in range(1, num):
#     if num % i == 0:
#         total += i

# if total == num:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")

# *********************************************************************************************************************

# prime or not 
# n=int(input("Enter a number: "))
# count=0

# for i in range(1,n+1):
#     if n%i==0 :
#         count+=1

# if count ==2:
#     print("Prime number")
# else:
#     print("Not a Prime Number")

# ******************************************************************************************************************************

##reverse a string
# str1="DHIRAJ"
# str2 =""
# for i in range(len(str1)-1,-1,-1):
#     str2+=str1[i]


# ******************************************************************************************************************************


# str1 =input("Enter a string: ")
# str2=""

# for i in range(len(str1)-1,-1,-1):
#     str2+=str1[i]

# if str2 == str1:
#     print(f"{str1} is pallindrome")

# else :
#     print("not pallindrome")


# a="aecs@345224@*^$^@dvdfgbrvxc adv"
# char=0
# digt=0
# spchr=0

# for i in a:
#     if i.isdigit():
#         digt+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr+=1


# print("character count ",char)
# print("special character count ",spchr)
# print("digit count ",digt)


# ******************************************************************************************************************************


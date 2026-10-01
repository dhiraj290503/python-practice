# a =1

# while a <=10:
#     print(a)
#     a+=1

a=int(input("Enter number: "))
rev=0
while a > 0:
    rev = rev*10 + a%10
    a = a//10

print(rev)
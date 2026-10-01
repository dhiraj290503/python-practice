## list propeties 
## 1. Mutable
## 2. allows duplicates
## 3. heterogenous
## 4. ordered
## 5. 

###############################################################################################3

# list1=[1,2,3,4,5,5,"dj",True,2.3,print("hii")]

# print(list1)

###################################################################################################

"""list sclicing"""
# list1=[1,2,3,4,5,5,"dj",True,2.3,print("hii")]

# print(list1[0:4])

###################################################################################################

"""list traversing"""

# a=[10,11,12,13,14]

# for i in range(len(a)):
#     print(i,end=" ")
#     print(a[i])


# # or 

# for i in a:
#     print(i)

"""List Methods / Finctions"""

## 1.append
## 2.clear
## 3.remove
## 4.insert
## 5.extend
## 6.pop

# l=[1,2,3,4,5]

# l.append(10)
# print(l)

# l.remove(5)
# print(l)

# l.insert(0,11)
# print(l)

# l.pop()
# print(l)
 
# l[0]=111
# print(l)

# l.extend([10,20,30])
# print(l)

########################################################33

# l=[-29,-32,22,221,-54,-32,15,0,-4]
# pl=[]
# nl=[]

# for i in range(len(l)):
#     if l[i] >= 0:
#         pl.append(l[i])
#     else:
#         nl.append(l[i])

# print("positive list",pl)
# print("negative list",nl)



# def positive_numbers(l):
#     print("Positive elements are:")
#     for i in range(len(l)):
#         if l[i] >= 0:
#             print(l[i])

# def negative_numbers(l):
#     print("Negative elements are:")
#     for i in range(len(l)):
#         if l[i] < 0:
#             print(l[i])


# l=[-29,-32,22,221,-54,-32,15,0,-4]

# positive_numbers(l)
# negative_numbers(l)
        

########################################################################################################3

# mean of list 
# listt1=[1,10,2,20,3,30]
# sum=0
# mean=""
# count = len(listt1)

# for i in range(len(listt1)):
#     sum += listt1[i]


# mean = sum/count

# print("Mean of list is ",mean)
##############################################################################################################3
#greatest element with its index 

# listt1=[11,1001,10,2,20,3,30]
# greatest=0
# index=0
# for i in range(len(listt1)):
#     if listt1[i] > greatest:
#         greatest=listt1[i]
#         index=i
        

# print(f"largest number is {greatest} on index {index}")

# list1 = [11, 1001, 10, 2, 20, 3, 30]

# greatest = list1[0]
# second = list1[0]

# for num in list1:
#     if num > greatest:
#         second = greatest
#         greatest = num
#     elif num > second and num != greatest:
#         second = num

# print("Largest:", greatest)
# print("Second largest:", second)


# list1 = [11, 1001, 10, 2, 20, 3, 30]
list1 = [1,2,3,4,5]
list1 = [5,4,3,2,1]

for i in range(len(list1)-1):
    if list1[i] < list1[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else :
    print("Your list is sorted")
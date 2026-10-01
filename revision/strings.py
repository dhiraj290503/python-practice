"""Strings"""

# a="svdksjbvkd  dvbhsadbv avfviuv v iusdhfv fvua vd"

# a="A"

# print(ord(a))

# a = 65

# print(chr(65))

"""String Indexing"""
#postivie indexing ==> right to left > 1,2,3,4...
#negative indexing ==> left to right > ...,-4,-3,-2,-1

# a= "brother"

# print(a[0],a[-7])
# print(a[1],a[-2])
# print(a[2])
# print(a[3])

# print(a[7])  #IndexError: string index out of range


"""string slicing"""
# a[start:stop:steps]

# b = "hello brother"
# print(b[0:5:1])
# print(b[6:13:1])
# print(b[6::1])
# print(b[6::])
# print(b[::])
# print(b[::-1])


"""type conversion"""

a="hello Im Dhiraj"
b=23

print(type(b),b)

c=str(b)
print(type(c),c)

d=int(c)
print(type(d),d)

# falsey values
# 1. false 
# 2. 0
# 3. 0.0
# 4. ""
# 5. []
# 6. ()
# 7> {}
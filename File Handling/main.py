"""how to open file"""

# # p = open(r'D:\sheryians DS\python\File Handling\main.py')
# p = open(r'main.py')

# print(p.read()) 

"""Modes to open file"""
## r => reads the file (file must exist)
## w => writes => creates file or overrites
## a => append -> adds to end of line
## x => creates -> creates a new file, fails if file exists

"""w"""
# r = open("dj.txt",'w')

# r.write("Hello this is dhiraj and im writing in this file")

# r.close()

######################################################################################################################

"""a"""
# r = open("dj1.txt",'a')

# r.write("Hello this is dhiraj and im writing in this file")

# r.close()
r = open("dj1.txt",'a')

r.write(" and now using 'a' im writing a new content")

r.close()
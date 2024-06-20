# import os 
# import os.path
# import shutil

# a=os.listdir('.')
# print(a)



file=open("a.txt", 'a')
file.write("\nhi i am hacker \n")
file=open("a.txt", 'r')
cont=file.readlines()
print(cont)
file.close()
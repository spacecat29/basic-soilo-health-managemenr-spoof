import os 
cwd = os.getcwd() 
print("Current working directory:", cwd) 
print("---------------------------------------")

import os 
def current_path():   
    print("Current Working Directory Before")
    sexy_cwd = os.getcwd()
    print(sexy_cwd)
    print()
current_path()
os.chdir('../')
current_path()

print("----------------------------------------")
import os
directory = "python_roject"
parent_dir = "G:\Python"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print(f"Directory {directory} created")

directory = "Noob Aster"
parent_dir = "G:\Python"
mode = 0o666
path = os.path.join(parent_dir,directory)
os.mkdir(path,mode)
print(f"New Directory {directory} Created Motherfucker")


print("-------------------------------------------")

import os
directory = "Vadapav"
parent_dir = "G:\Python\\python_project"
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print(f"Directory {directory} created")

directory = "PocketPython"
parent_dir = "G:\Python\\Noob MAster"
mode = 0o666
path = os.path.join(parent_dir,directory)
os.makedirs(path,mode)
print(f"New Directory {directory} Created Motherfucker")


print("---------------------------------------------")

import os
path = "/"
dir_list = os.listdir(path)
print("Files ANd Directories In '",path,"'  :")
print(dir_list)

print("----------------------------------------------")

import os 
file_name = "noob master.txt"
location = 'G:\Python\python_project'
path_dalit = os.path.join(location,file_name)
os.remove(path_dalit)

import os 
directory_name = "python_project"
location = "G:\Python"
path_dallit_2 = os.path.join(location,directory_name)
os.rmdir(path_dallit_2)

print("----------------------------------------------")

import os

try:
    filename = 'data_handling.txt'
    fo = open(filename,'rU')
    fo.read() 
    fo.close()
except IOError:
    print('Problem Reading', filename)
print("-------------------------------------")

import os 
 
filename = "padu.txt"
write_it = open(filename,'w')
write_it.write('Hello Sexy')
write_it.close()
read_it = open(filename,'r')
print(read_it.read())

file_name = os.popen(filename, 'w')
file_name.write("Hello mew sexy")
print("------------------------------------")

import os
fd = "GFG.txt"
file = open(fd, 'r')
text = file.read()
print(text)
os.close(file)

print("------------------------------------")

import os
fd = "GFG.txt"
os.rename(fd,'New.txt')
os.rename(fd,'New.txt')

print("------------------------------------")

import os #importing os module.
os.remove("file_name.txt") #removing the file.

print("-------------------------------------")

import os 
#importing os module

result = os.path.exists("file_name") #giving the name of the file as a parameter.

print(result)

print('--------------------------------------')


import os #importing os module
size = os.path.getsize("Exception Handling.py")
print("Size of the file is", size," bytes.")
import os 

os.mkdir('meri_direcory')
os.makedirs('G:\Python\directory_management.py')

print("---------------------------------")

import os 

print('Current Directory', os.getcwd())
print("Byte String format",os.getcwdb())

print("-----------------------------------")

import os 

os.rename("renamed_directory", "meri_directory")

import os

os.renames('my_directory', 'renamed_directory')

print("-----------------------------------")

import os

print("Current directory :", os.getcwd())

# Changing directory
os.chdir('/home/nikhil/Desktop/')
print("Current directory :", os.getcwd())

print("-------------------------------------")

import os

list_that_fuck = "files in Current Worimk Directory"
print(list_that_fuck,os.listdir(os.getcwd()))

print('--------------------------------------')

import os

li=os.listdir('/')

if len(li)==0:
  print("Error!! Directory not empty!!")
else:
  os.rmdir('k:/files')

print('--------------------------------------')

import os

# current working directory of
# GeeksforGeeks
cwd='/'
print(os.path.isdir(cwd))

# Some other directory
other='K:/'
print(os.path.isdir(other))

print('--------------------------------------')

import os 

ist = '/'
print(os.path.isdir(ist)) 

cwd = 'K:/'
print(os.path.isdir(cwd))

print('--------------------------------------')

import os 

print(os.path.getsize(os.getcwd()))

print('--------------------------------------')

import time 
import os

current_time = os.path.getatime('/')
modification_time = os.path.getmtime('/')

print('Current Time:',time.ctime(current_time))
print('Current Time:',time.ctime(modification_time))

print('--------------------------------------')

import shutil

# Copy the entire directory tree
shutil.copytree("source_dir", "destination_dir")
print("Directory copied successfully")

print('---------------------------------------')

import shutil

# Remove a directory tree
shutil.rmtree("destination_dir")
print("Directory removed successfully")

print("----------------------------------------")

import shutil

# Move a directory to a new location
shutil.move("source_dir", "new_location")
print("Directory moved successfully")
from pathlib import Path 

path = Path("/")

for eachone in path.iterdir():
    if eachone.is_dir():
        print(eachone)

print("---------------------------")

from pathlib import Path

potty = Path('/')

file_identyfy = potty.rglob('*py')
for scan in file_identyfy:
    print(scan)

print('----------------------------')

from pathlib import Path

potty = Path('/')

file_identyfy = potty.rglob('*py')
for scan in file_identyfy:
    print(scan)

lo = potty / 'example.py'
print(lo)

print("Is Absolute:", lo.is_absolute())
print("File name:", lo.name)
print("Extension:", lo.suffix)

print("Parent directory:", lo.parent)

print('----------------------------')


from pathlib import Path

# Define the path object
path = Path('G:/Python')  # Specify the correct directory path

# Reading from a file
with (path / 'file handling.txt').open('r') as file:
    content = file.read()
    print(content)

# Writing to a file
with (path / 'file handlin2.txt').open('w') as file:
    file.write("Hello, GFG!")

print("-------------------------------")
print("-----------------------Pure Path---------------")

from pathlib import PurePath

obj = PurePath('foo/bar')
print(obj)

print("-------------------------------")

# Import PurePosixPath class for macOS and Linux
# from pathlib module
from pathlib import PurePosixPath

# Instantiate the PurePosixPath class
obj = PurePosixPath('foo/bar')

# print the instance of PurePosixPath class
print(obj)

print("-------------------------------")

# Import PureWindowsPath class for windows
# from pathlib module
from pathlib import PureWindowsPath

# Instantiate the PureWindowsPath class
obj = PureWindowsPath('foo/bar')

# print the instance of PureWindowsPath class
print(obj)

print("-------------------------------")

from pathlib import PurePath

path_file = PurePath('G:\Python\Exception Handling.py')
print(path_file.is_absolute())

path_file = PurePath('delete.txt')
print(path_file.is_absolute())

print("-------------------------------")
from pathlib import PurePath

filename = 'G:\Python\\file handling.txt'

obj = PurePath(filename)

comp = obj.name
print(comp)

print('---------------------------------------')

# Import the Path class
from pathlib import Path

# Instantiate the Path class
obj = Path('/usr/local/bin')

print(obj)

print('----------------------------------')

# Import the Path class
from pathlib import Path

# Instantiate the Path class
obj = Path('/usr/local/bin')

print(obj)

print("-------------------------------------------")

# Import PosixPath class
# from pathlib module
from pathlib import PosixPath

# Instantiate the PosixPath class
obj = PosixPath('/usr/local/bin')

# Print the instance of PosixPath class
print(obj)

print("---------------------------------------------")

# Import WindowsPath class
# from pathlib module
from pathlib import WindowsPath

# Instantiate the WindowsPath class
obj = WindowsPath('C:/Program Files/')

# Print the instance of WindowsPath class
print(obj)

print("---------------------------------------------")

# Import WindowsPath class
# from pathlib module
from pathlib import WindowsPath

# Instantiate the WindowsPath class
obj = WindowsPath('C:/Program Files/')

# Print the instance of WindowsPath class
print(obj)

print("---------------------------------------------")

# Import Path class
from pathlib import Path

# Get the current working directory name
dir = Path.cwd()

print(dir)

print("---------------------------------------------")


# Import Path class
from pathlib import Path

# Path
path = '/home/hrithik/Desktop'

# Instantiate the Path class
obj = Path(path)

# Check if path points to
# an existing file or directory
print(obj.exists())

print("---------------------------------------------")


# Import Path class
from pathlib import Path

# Path
path = '/home/hrithik/Desktop'

# Instantiate the Path class
obj = Path(path)

# Check if path refers to
# directory or not
print(obj.is_dir())

print("---------------------------------------------")


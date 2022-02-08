
# import os
# # Get the current working directory
# cwd=os.getcwd()

# print("current working directory:",cwd)

# # ***************************
# # changing the current working directory

# import os

# # function to get the current working directory
# def current_path():
#     print("current working directory before")
#     print(os.getcwd())
#     print()

# # printing CWD before 
# current_path()

# # Changing the CWD
# os.chdir('../')

# # Printing CWD after
# current_path()
# # ************************************

# creating a directory
# os.mkdir()
# os.makedirs()

import os
directory="GeeksforGeeks"

# parent directory path
parent_dir = "D:/Pycharm projects/"
 
# Path
path = os.path.join(parent_dir, directory)
 
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)
 
# Directory
directory = "Geeks"
 
# Parent Directory path
parent_dir = "D:/Pycharm projects"
 
# mode
mode = 0o666
 
# Path
path = os.path.join(parent_dir, directory)
 
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
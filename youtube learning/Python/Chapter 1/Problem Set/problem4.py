import os

# specify the directory path
path = "/"

# get the list of files and directories
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)
# 5. Write a program which finds out whether a given name is present in a list or not.

lis = ["aditya","arif","anaj","amir","asish","aniket","aritra"]

name = input("Enter the name: ").lower()

if(name in lis):
  print(f"{name.upper()} -> Present")
else:
  print(f"{name.upper()} is not in the list")

# OUTPUT:
"""
Enter the name: ARif
ARIF -> Present

"""
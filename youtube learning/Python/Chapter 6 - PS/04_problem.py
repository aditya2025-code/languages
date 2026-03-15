# 4. Write a program to find whether a given username contains less than 10 characters or not.

name = input("Enter your name: ")

if(len(name)<10):
  print(f"{name} contains less than 10 characters")
else:
  print(f"{name} contains more than or equal to 10 characters")

# OUTPUT:
"""
Enter your name: ADI
ADI contains less than 10 characters

"""
# 1. Write a program to find the greatest of four numbers entered by the user

a = int(input("Enter the no. : "))
b = int(input("Enter the no. : "))
c = int(input("Enter the no. : "))
d = int(input("Enter the no. : "))

if (a > b and a > c and a > d):
  print(f"{a} is Greatest Number")
elif (b > a and b > c and b > d):
  print(f"{b} is Greatest Number")
elif (c > a and c > b and c > d):
  print(f"{c} is Greatest Number")
else:
  print(f"{d} is Greatest Number")

# OUTPUT:
"""
Enter the no. : 2
Enter the no. : 5
Enter the no. : 3
Enter the no. : 1
5 is Greatest Number

"""
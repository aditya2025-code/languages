# 10. Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter the number: "))

for i in range(1,11):
  print(f"{n} X {11-i} = {(11-i)*n}")
  i += 1
  
# OUTPUT:
"""
Enter the number: 11
11 X 10 = 110
11 X 9 = 99
11 X 8 = 88
11 X 7 = 77
11 X 6 = 66
11 X 5 = 55
11 X 4 = 44
11 X 3 = 33
11 X 2 = 22
11 X 1 = 11

"""  
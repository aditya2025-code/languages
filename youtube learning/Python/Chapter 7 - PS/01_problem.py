# 1. Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter the number: "))

for i in range(1,11):
  print(f"{n} X {i} = {n*i}")

# OUTPUT:
"""
Enter the number: 9
9 X 1 = 9
9 X 2 = 18
9 X 3 = 27
9 X 4 = 36
9 X 5 = 45
9 X 6 = 54
9 X 7 = 63
9 X 8 = 72
9 X 9 = 81
9 X 10 = 90

"""
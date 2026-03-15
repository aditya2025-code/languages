# 6. Write a program to calculate the factorial of a given number using for loop.

n = int(input("Enter the number: "))
facto = 1

for i in range(1,n+1):
  facto *= i

print(f"Factorial of {n} = ",facto)

# OUTPUT:
"""
Enter the number: 5
Factorial of 5 =  120

"""
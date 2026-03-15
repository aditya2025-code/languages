# 5. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number: "))
i = 1
sum = 0

while i <= n:
  sum += i
  i += 1

print(f"sum of first {n} natural numbers is ",sum)

# OUTPUT:
"""
Enter the number: 10
sum of first 10 natural numbers is  55

"""
# 4. Write a recursive function to calculate the sum of first n natural numbers

def sum_of_n(n):
  if(n==1):
    return 1
  return n + sum_of_n(n-1)

n = int(input("Enter the no: "))

print(f"Sum of first {n} natural no. is {sum_of_n(n)}")

# OUTPUT:
"""
Enter the no: 5
Sum of first 5 natural no. is 15

"""  
# 4. Write a program to find whether a given number is prime or not.

n = int(input("Enter the number: "))

for i in range(2,n):
  if(n % i == 0):
    print(f"{n} is not prime no.")
    break
else:
  print(f"{n} is Prime no.")

# OUTPUT:
"""
Enter the number: 7
7 is Prime no.

"""
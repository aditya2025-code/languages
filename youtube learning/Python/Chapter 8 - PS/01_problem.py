# 1. Write a program using functions to find greatest of three numbers.

def greatest_three():
  a = int(input("Enter the no: "))
  b = int(input("Enter the no: "))
  c = int(input("Enter the no: "))
  if(a > b and a > c):
    print(f"{a} is the greatest")
  elif(b > a and b > c):
    print(f"{b} is the greatest")
  else:
    print(f"{b} is the greatest")

print("Start")
greatest_three()
print("End")

# OUTPUT:
"""
Start
Enter the no: 5
Enter the no: 4
Enter the no: 1
5 is the greatest
End

"""  
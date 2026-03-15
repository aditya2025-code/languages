# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def down_pattern(n):
  if(n==0):
   return
  print("*"*n)
  down_pattern(n-1)

n = int(input("Enter the no: "))
down_pattern(n)

# OUTPUT:
"""
Enter the no: 5
*****
****
***
**
*

"""  
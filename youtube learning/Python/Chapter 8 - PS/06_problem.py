# 6. Write a python function which converts inches to cms

def inch_to_cm(inch):
  return inch* 2.54

inch = float(input("Enter inch: "))
print(f"{inch} inch = {round(inch_to_cm(inch),2)} cm ")

# OUTPUT:
"""
Enter inch: 55.4
55.4 inch = 140.72 cm 

"""  
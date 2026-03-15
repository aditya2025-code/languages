# 2. Write a python program using function to convert Celsius to Fahrenheit.

def cel_to_fahr(cel):
  f = (cel * 9/5) + 32
  return f

celsius = int(input("Enter temperature in celsius: "))

print(f"{celsius}°C = {cel_to_fahr(celsius)}°F")

# OUTPUT:
"""
Enter temperature in celsius: 25
25°C = 77.0°F

"""  
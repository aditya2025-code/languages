# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter the marks: "))
marks2 = int(input("Enter the marks: "))
marks3 = int(input("Enter the marks: "))

total_persentage = ( 100 * ( marks1 + marks2 + marks3 )) / 300

if ( total_persentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
  print("You passed!, \ntotal persentage: ",total_persentage)
else:
  print("You failed!")

# OUTPUT:
"""
Enter the marks: 56
Enter the marks: 87
Enter the marks: 74
You passed!, 
total persentage:  72.33333333333333

"""
# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = []

m = int(input("Enter Marks: "))
marks.append(m)
m = int(input("Enter Marks: "))
marks.append(m)
m = int(input("Enter Marks: "))
marks.append(m)
m = int(input("Enter Marks: "))
marks.append(m)
m = int(input("Enter Marks: "))
marks.append(m)
m = int(input("Enter Marks: "))
marks.append(m)

marks.sort()

print(marks)

# OUTPUT:
"""
Enter Marks: 50
Enter Marks: 60
Enter Marks: 25
Enter Marks: 80
Enter Marks: 33
Enter Marks: 90
[25, 33, 50, 60, 80, 90]

"""
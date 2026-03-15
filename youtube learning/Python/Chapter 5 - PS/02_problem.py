# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set()

n = int(input("Enter The no.: "))
s.add(n)
n = int(input("Enter The no.: "))
s.add(n)
n = int(input("Enter The no.: "))
s.add(n)
n = int(input("Enter The no.: "))
s.add(n)
n = int(input("Enter The no.: "))
s.add(n)
n = int(input("Enter The no.: "))
s.add(n)
n = int(input("Enter The no.: "))
s.add(n)
n = int(input("Enter The no.: "))
s.add(n)

print(s)

# OUTPUT:
"""
Enter The no.: 1
Enter The no.: 2
Enter The no.: 2
Enter The no.: 3
Enter The no.: 1
Enter The no.: 3
Enter The no.: 4
Enter The no.: 5
{1, 2, 3, 4, 5}

"""
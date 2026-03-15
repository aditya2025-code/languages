# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dic = {}

name = input("Enter your name: ")
lang = input("Enter language: ")
dic.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter language: ")
dic.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter language: ")
dic.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter language: ")
dic.update({name:lang})

print(dic)

# OUTPUT:
"""
Enter your name: Adi
Enter language: C
Enter your name: Asish
Enter language: C++
Enter your name: Arif
Enter language: HTML
Enter your name: Anaj
Enter language: Python
{'Adi': 'C', 'Asish': 'C++', 'Arif': 'HTML', 'Anaj': 'Python'}

"""
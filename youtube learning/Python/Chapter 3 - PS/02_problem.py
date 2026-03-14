# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>",input("Enter your name: ")).replace("<|Date|>",input("Enter the date: ")))

# OUTPUT:
"""
Enter your name: Aditya
Enter the date: 14.03.26

Dear Aditya,
You are selected!
14.03.26

"""
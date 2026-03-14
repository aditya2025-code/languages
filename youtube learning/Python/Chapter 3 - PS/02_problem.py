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
print(letter.replace("<|Name|>","Adi").replace("<|Date|>","14.03.26"))

# OUTPUT:
"""

Dear Adi,
You are selected!
14.03.26


"""
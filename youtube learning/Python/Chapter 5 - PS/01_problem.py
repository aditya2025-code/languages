# 1. Write a program to create a dictionary of Bengali words with values as their English translation. Provide user with an option to look it up!

dic = {
  "sahajo":"help",
  "khaua":"eat",
  "hata":"walk"
}

word = input("Enter the key word of meaning:")

print(f"{word} = {dic[word]}")

# OUTPUT:
"""
Enter the key word of meaning:khaua
khaua = eat

"""
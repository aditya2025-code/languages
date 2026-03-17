# Stone , Paper , Scissor GAME

import random

def fun_game():

  computer = random.choice(["stone","paper","scissor"])

  user = input("Choose (Stone or Paper or Scissor): ").lower()

  lis = ["stone","paper","scissor"]

  if(user in lis):
    print(f"Computer choose = {computer}\nYou choose = {user}")
    if(user == computer):
      print("Ohh! It's draw")
    elif(user == "stone" and computer == "paper"):
      print("Computer win")
    elif(user == "paper" and computer == "stone"):
      print("You win")
    elif(user == "scissor" and computer == "paper"):
      print("You win")
    elif(user == "paper" and computer == "scissor"):
      print("Computer win")
    elif(user == "stone" and computer == "scissor"):
      print("You win")
    elif(user == "scissor" and computer == "stone"):
      print("Computer win")
    else:
      print("!Logical error!")
  else:
    print("Invalid input,\nOnly enter from this option\n\t(stone,paper,scissor)")
    return 1
  option = int(input("For play again enter 1\nAnd for end enter 0\n\t-> "))
  if(option == 1):
    return 1
  else:
    return 0

print("\t: Stone : Paper : Scissor : ")
play = 1
while(play):
  play = fun_game()

# OUTPUT:
"""
        : Stone : Paper : Scissor : 
Choose (Stone or Paper or Scissor): Stone
Computer choose = paper
You choose = stone
Computer win
For play again enter 1
And for end enter 0
        -> 1
Choose (Stone or Paper or Scissor): paper
Computer choose = stone
You choose = paper
You win
For play again enter 1
And for end enter 0
        -> 1
Choose (Stone or Paper or Scissor): sesor
Invalid input,
Only enter from this option
        (stone,paper,scissor)
Choose (Stone or Paper or Scissor): scissor
Computer choose = paper
You choose = scissor
You win
For play again enter 1
And for end enter 0
        -> 0

"""  
import random
import sys

playerchoice = input("enter \n1 for rock, \n2 for paper, or \n3 for scissor :\n\n")
player = int(playerchoice)
if player < 1 or player > 3: 
    sys.exit("you can only enter 1,2 or 3")  
   
print(f"you chose {playerchoice}")

computerchoice = random.choice("123")
computer = int(computerchoice)
print(f"computer chose {computer}")

if player == 1 and computer == 3:
    print(f"you win! 😂😂")
elif player == 2 and  computer == 1:
    print(f"you win! 😂😂")
elif player == 3 and computer == 2:
    print(f"you win! 😂😂")
elif player == computer :
    print(f"it is a tie 🥺🥺")
else : 
    print(f"computer wins! 🐍🐍")


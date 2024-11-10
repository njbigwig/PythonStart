#Rock, Paper,Scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

asciiart = [rock, paper, scissors]
rpschoices = ["r", "p", "s"]
artchoice = 0

# get player's choice
player_choice = input("What do you choose? r = rock, p = paper, s = scissors ")
print("You choose:")
if player_choice == "r":
    #print(rock)
    artchoice = 0
elif player_choice == "p":
    #print(paper)
    artchoice = 1
else:
    #print(scissors)
    artchoice = 2

print(asciiart[artchoice])
print("\n\n")

# get computer's choices
computer_choice = random.choice(rpschoices)
print("Computer choose:")
if computer_choice == "r":
    #print(rock)
    artchoice = 0
elif computer_choice == "p":
    #print(paper)
    artchoice = 1
else:
    #print(scissors)
    artchoice = 2
print(asciiart[artchoice])
print("\n\n")

# decide who won:
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if player_choice == computer_choice:
    # tie checking eliminates 2 compares in the nested if-else
    print("Tie, try again!")
elif player_choice == "r":
    # player has rock, compare against 2 computer choices
    if computer_choice == "p":
        print("You Lost!")
    else:
        # computer has scissor
        print("You Won!")  
elif player_choice == "p":
    if computer_choice == "r":
        # computer has rock
        print("You Won!")
    else:
        # computer has scissors
        print("You Lost!")
else:
    # player has scissors
    if computer_choice == "p":
        # computer has paper
        print("You Won!")
    else:
        # computer has rock
        print("You Lost!")





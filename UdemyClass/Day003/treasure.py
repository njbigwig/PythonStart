print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?\n")
leftORright = input("Type left or right: ")

if not leftORright == "left":
    print("You have fell into a hole. Game over.") 
else:
    print("You have come to a river. Do you want to swim across or wait for a boat?\n")
    swimORwait = input("Type swim or wait: ")

    if not swimORwait == "wait":
        print("You have been attacked by a giant trout. Game over.") 
    else:
        print("You have come to 3 colored doors. Which one do open?\n")
        whichdoor = input("Type red, yellow, blue: ")

        if whichdoor == "blue":
            print("You have been burned by fire. Game over.") 
        elif whichdoor == "blue":
            print("You have been eaten by beasts. Game over.") 
        elif whichdoor == "yellow":
            print("You win!") 
        else:
            print("Game over.") 
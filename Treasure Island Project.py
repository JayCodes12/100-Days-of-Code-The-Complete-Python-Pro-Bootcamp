print(r'''
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

left_or_right = input("Do you want to go left or right? Type L or R. ")
if left_or_right == "R":
    print("You fell into a hole :(. Game over.")
elif left_or_right == "L":
    swim_or_wait = input("Do you want to swim or wait? Type S or W. ")
    if swim_or_wait == "S":
        print("You were attacked by a trout! Game Over.")
    elif swim_or_wait == "W":
        door_choice = input("Which door do you want to enter, Red(R), Yellow(Y), or Blue(B)? Type R, Y, or B. ")
        if door_choice == "Y":
            print("Congratulations, You win!")
        elif door_choice == "R":
            print("Burned by fire. Game Over.")
        elif door_choice == "B":
            print("Eaten by beasts. Game Over.")
        else:
            print("Because you didn't enter a valid input, Game Over.")
    #For any inputs that isn't S or W
    else:
        print("Because you didn't enter a valid input, you were attacked by a trout. Game Over")
##For any inputs that aren't R or L
else:
    print("Because you didn't enter a valid input, you fell into a hole. Game Over.")
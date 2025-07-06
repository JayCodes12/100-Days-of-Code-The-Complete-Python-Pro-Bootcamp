import random

print("Welcome to Rock, Paper, Scissors! ")
#Determines the computer's choice
comp_choice = random.randint (0, 2)

#User Prompt
choice = input("What do you chose? "
               "Type 0 for Rock, 1 for "
               "Paper, or 2 for Scissors. \n")
if choice == "0":
    print("You chose: Rock")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

elif choice == "1":
    print("You chose: Paper")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif choice == "2":
    print("You chose: Scissors")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    #Prints an empty line so the error message isn't typed twice
    print()

#--------------------------Computer Choice--------------------------------------------
if comp_choice == 0:
    print("Computer chose: Rock")
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    ''')
elif comp_choice == 1:
    print("Computer chose: Paper")
    print('''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')
else:
    print("Computer chose: Scissors")
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
#-----------------------Determines if you Win or Lose------------------
#If you choose ROCK ------------------------------------
if choice == "0":
    if comp_choice == 0:
        print("It's a draw")
    elif comp_choice == 1:
        print("You lose.")
    else:
        print("You win!")
#If you choose PAPER ---------------------------------
elif choice == "1":
    if comp_choice == 0:
        print("You Win!")
    elif comp_choice == 1:
        print("Its a draw.")
    else:
        print("You lose.")
#If you choose SCISSORS ------------------------------
elif choice == "2":
    if comp_choice == 0:
        print("You lose.")
    elif comp_choice == 1:
        print("You win!")
    else:
        print("It's a draw.")
else:
    print("You chose something that is not 0, 1, or 2.")
#print("Rock, Paper, Scissors, Shoot!")

import random

print("-------------------")
print("Welcome to my Rock-Paper-Scissors game...")
print("-------------------")

#USER CHOICE
options = ["rock", "paper", "scissors"]
user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")
if user_choice in options:
    print("You chose: ", user_choice)
else:
    print("OOPS - Invalid Selection")    

#COMPUTER'S CHOICE

computer_choice = random.choice(options)

print("The computer chose: ", computer_choice)

print("-------------------")
#DETERMINING THE WINNER
#THE RULES ARE AS FOLLOWS:

    # Rock beats Scissors
    # Paper beats Rock
    # Scissors beats Paper
    # Rock vs Rock, Paper vs Paper, and Scissors vs Scissors each results in a "tie"

if user_choice == "rock" and computer_choice == "rock":
        print("It's a tie!")
elif user_choice == "rock" and computer_choice == "paper":
        print("Sorry, you lose")
elif user_choice == "rock" and computer_choice == "scissors":
        print("Congrats, you won!")    

if user_choice == "paper" and computer_choice == "rock":
        print("Congrats, you won!")
elif user_choice == "paper" and computer_choice == "paper":
         print("It's a tie!")
elif user_choice == "paper" and computer_choice == "scissors":
        print("Sorry, you lose")

if user_choice == "scissors" and computer_choice == "rock":
        print("Sorry, you lose")
elif user_choice == "scissors" and computer_choice == "paper":
        print("Congrats, you won!")
elif user_choice == "scissors" and computer_choice == "scissors":
         print("It's a tie!")

print("-------------------")
print("Thanks for playing. Please play again!")


#SAMPLE OUTPUT:

# -------------------
# Welcome to my Rock-Paper-Scissors game...
# -------------------
# Please choose either 'rock', 'paper', or 'scissors': rock
# You chose: 'rock'
# The computer chose: 'paper'
# -------------------
# Oh, the computer won. It's ok.
# -------------------
# Thanks for playing. Please play again!
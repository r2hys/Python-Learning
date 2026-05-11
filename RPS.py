#Rock / paper / scissors game
import random

computer_choice = random.choice(["rock", "paper", "scissors"])
user_choice = input("Please pick either rock, paper or scissors\n").lower()

if computer_choice == user_choice:
    print("It is a Tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You have won!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You have won!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You have won!")
else:
    print("You have lost! The computer went with " + computer_choice)



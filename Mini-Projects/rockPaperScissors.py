import random

while True:
    choice = ["rock", "paper", "scissor"]

    computer = random.choice(choice)
    player = None

    while player not in choice:
        player = input("rock, paper or scissors?: ")

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie!")

    elif player == "paper" and computer == "scissors" or player =="rock" and computer =="paper" or player =="scissor" and computer =="paper":
        print("Computer: ", computer)
        print("Player: ", player)
        print("Oooopppss:(")

    elif player =="scissor" and computer =="paper" or player =="paper" and computer =="rock" or player =="rock" and computer =="scissor":
        print("Computer: ", computer)
        print("Player: ", player)
        print("Kangrachulason!")


    play_again = input("Play again? (yes/no): ")

    if play_again != "yes":
        break

print("Well Played!!!")

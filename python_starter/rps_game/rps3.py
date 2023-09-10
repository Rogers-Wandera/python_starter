import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerinput = input(
        "Choose 1 for Rock \nChoose 2 for Paper \nChoose 3 for Scissors \n")
    if (playerinput not in ["1", "2", "3"]):
        "Please choose 1, 2, or 3 🤦"
        play_rps()

    player = int(playerinput)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You chose: " + str(RPS(player)).replace("RPS.", "") +
          "\nComputer chose: " + str(RPS(computer)).replace("RPS.", ""))
    print("")

    if player == 1 and computer == 3:
        print("Player wins 😍")
    elif player == 2 and computer == 1:
        print("Player wins ❤")
    elif player == 3 and computer == 2:
        print("Player wins 😎")
    elif player == computer:
        print("Its a tie 😱")
    else:
        print("Computer wins 🙈")

    while True:
        playerres = input("Enter Y for Yes and N for No: \n")
        if (playerres.lower() not in ["y", "n"]):
            continue
        else:
            break

    if (playerres.lower() == "y"):
        play_rps()
    else:
        print("\nThank you for playing 🥂\n")
        print("Until next time 😎")
        sys.exit("Byeeeeeeee 👋")


play_rps()

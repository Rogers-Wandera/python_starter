import sys
import random
from enum import Enum

game_count = 0


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerinput = input(
        "Choose 1 for Rock \nChoose 2 for Paper \nChoose 3 for Scissors \n")
    if (playerinput not in ["1", "2", "3"]):
        print("Please choose 1, 2, or 3 🤦")
        play_rps()

    player = int(playerinput)

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You chose: " + str(RPS(player)).replace("RPS.", "") +
          "\nComputer chose: " + str(RPS(computer)).replace("RPS.", ""))
    print("")

    def game_results(player, computer):
        if player == 1 and computer == 3:
            return "Player wins 😍"
        elif player == 2 and computer == 1:
            return "Player wins 😍"
        elif player == 3 and computer == 2:
            return "Player wins 😍"
        elif player == computer:
            return "Its a tie 😱"
        else:
            return "Computer wins 🙈"

    game_response = game_results(player, computer)
    print(game_response)

    global game_count
    game_count += 1

    print("\n Game has been played: " + str(game_count))

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

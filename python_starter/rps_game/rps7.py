import sys
import random
from enum import Enum


def rps():

    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        nonlocal player_wins
        nonlocal computer_wins

        playerinput = input(
            "Choose 1 for Rock \nChoose 2 for Paper \nChoose 3 for Scissors \n")
        if (playerinput not in ["1", "2", "3"]):
            print("Please choose 1, 2, or 3 🤦")
            play_rps()

        player = int(playerinput)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("")
        print(
            f"You chose {str(RPS(player)).replace('RPS.', '')} \nComputer chose {str(RPS(computer)).replace('RPS.', '')}")
        print("")

        def game_results(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "Player wins 😍"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "Player wins 😍"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "Player wins 😍"
            elif player == computer:
                return "Its a tie 😱"
            else:
                computer_wins += 1
                return "Computer wins 🙈"

        game_response = game_results(player, computer)
        print(game_response)

        nonlocal game_count
        game_count += 1

        print(f"\n Game has been played {str(game_count)}")
        print(f"\n Player wins: {str(player_wins)}")
        print(f"\n Compuer wins: {str(computer_wins)}")

        while True:
            playerres = input("\nEnter Y for Yes and N for No: \n")
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

    return play_rps


rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()

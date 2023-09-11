import sys
import random
from enum import Enum


def rps(name="PlayerOne"):

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
        nonlocal name

        playerinput = input(
            f"{name}, Please choose 1 for Rock \nchoose 2 for Paper \nchoose 3 for Scissors \n")
        if (playerinput not in ["1", "2", "3"]):
            print(f"{name}, please choose 1, 2, or 3 🤦")
            play_rps()

        player = int(playerinput)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("")
        print(
            f"{name} you chose {str(RPS(player)).replace('RPS.', '')} \nComputer chose {str(RPS(computer)).replace('RPS.', '')}")
        print("")

        def game_results(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal name
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name} wins 😍"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name} wins 😍"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name} wins 😍"
            elif player == computer:
                return "Its a tie 😱"
            else:
                computer_wins += 1
                return "Computer wins 🙈"

        game_response = game_results(player, computer)
        print(game_response)

        nonlocal game_count
        game_count += 1

        print(f"\n Game has been played {game_count}")
        print(f"\n {name} wins: {player_wins}")
        print(f"\n Compuer wins: {computer_wins}")

        while True:
            playerres = input(f"\n{name} Enter Y for Yes and N for No: \n")
            if (playerres.lower() not in ["y", "n"]):
                continue
            else:
                break

        if (playerres.lower() == "y"):
            play_rps()
        else:
            print("\nThank you for playing 🥂\n")
            print("Until next time 😎")
            sys.exit(f"{name} Byeeeeeeee 👋")

    return play_rps


if __name__ == "__main__":
    import argparse

    Parser = argparse.ArgumentParser(
        description="Provides personalized game experience."
    )
    Parser.add_argument(
        "--version" "-v", action="version", version="%(prog)s 1.0"
    )
    Parser.add_argument(
        "--name", "-n", metavar="name", required=True, help="The name of the person to play the game"
    )
    args = Parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()

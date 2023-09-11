import sys
from enum import Enum
from random import choice
import math


def GuessNumber(name="Player One"):
    player_wins = 0
    game_played = 0
    playerrating = 0
    playerwinstate = False

    def playGame():
        nonlocal name
        nonlocal player_wins
        nonlocal game_played
        nonlocal playerrating
        nonlocal playerwinstate

        class GN(Enum):
            ONE = 1
            TWO = 2
            THREE = 3

        player_input = input(
            f"\n{name} please guess the number am thinking of between 1 and 3: \n")
        if player_input not in ["1", "2", "3"]:
            print(f"{name} please choose 1, 2, or 3 🤦")
            playGame()

        player = int(player_input)
        computer_choice = choice("123")
        computer = int(computer_choice)

        print(
            f"\n{name} you chose {str(GN(player)).replace('GN.','')}\nComputer chose {str(GN(computer)).replace('GN.', '')}\n")

        def gameResults(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal playerrating
            nonlocal playerwinstate

            if player == computer:
                player_wins += 1
                playerwinstate = True
                playerrating = (player/computer)*100
                return f"Wow {name} you are a genius 🤩"
            else:
                playerrating = (player/3)*100
                playerwinstate = False
                return f"Computer wins 🙈"

        game_response = gameResults(player, computer)
        print(game_response)

        nonlocal game_played
        game_played += 1
        print(f"\nGame has been played {game_played} times\n")
        if playerwinstate:
            print(f"\n{name} your wins are {player_wins}")
        else:
            print(f"\n😢😢 Please choose again hope you get it right\n")
        print(f"\n{name} Your Thinking capacity is {math.floor(playerrating)}%")

        while True:
            playerres = input("\nWould you like to play again? (y/n): ")
            if (playerres.lower() not in ['y', 'n']):
                continue
            else:
                break

        if playerres.lower() == 'y':
            playGame()
        else:
            print("\nThanks for playing! 🥂")
            print(f"\n{name} Byeeeee! 👋")
            sys.exit()
    return playGame


if (__name__ == "__main__"):
    import argparse
    Parser = argparse.ArgumentParser(
        description="Provides personalized game experience.")
    Parser.add_argument("-n", "--name", metavar="name", required=True,
                        help="The name of the person to play the game")
    Parser.add_argument("-v", "--version", action="version",
                        version="%(prog)s 1.0")
    args = Parser.parse_args()
    guess = GuessNumber(args.name)
    guess()

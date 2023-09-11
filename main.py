from python_starter.rps_game.rps8 import rps
from python_starter.challenges.guessnumber import GuessNumber
import argparse


def ArcadeGame(name):
    print(
        f"\n{name} please choose the game you want to play\n")

    print("\nChoose 1 for Guess Number Game\nChoose 2 for Rock Paper Scissors Game\n")
    userchoice = input(f"\nChoose either 1 or 2: ")
    if userchoice not in ["1", "2"]:
        print("Please choose 1 or 2 🤦")
        ArcadeGame(name)

    if userchoice == "1":
        guess = GuessNumber(name)
        guess()
    elif userchoice == "2":
        playRPS = rps(name)
        playRPS()


Parser = argparse.ArgumentParser(
    description="Provides personalized game experience."
)
Parser.add_argument(
    "-n", "--name", metavar="name", required=True,
    help="Provides name to be used in the game"
)
args = Parser.parse_args()
ArcadeGame(args.name)

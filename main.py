from typing import List
import argparse

from ui import GameUI
from engine import GameEngine


def startLobby():
    print(f"\nWelcome to Arrows-cli !\n")
    formatInput = input("Selection game: x01: ")
    playerInput = input("List players > ")
    players = playerInput.split(" ")
    form = int(formatInput)
    return (form, players)


def endLobby():
    again = input("Play a different game? [y/N] > ")
    # if again[0].lower()
    return


def main():
    target, players = startLobby()
    while True:
        engine = GameEngine(target, players)
        ui = GameUI(engine)
        ui.start()
        if not ui.replay():
            break


if __name__ == "__main__":
    main()

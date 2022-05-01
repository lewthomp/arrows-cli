from typing import List, Dict
import time
import csv


class GameEngine:
    """
    Represents a single match of x01 darts.
    """

    _SCORE_MAP = {"s": 1, "d": 2, "t": 3}
    _RESULT_MAP = {0: "BUST", 1: "SCORE", 2: "FINISH"}

    def __init__(self, target, players=[]):
        self.players = [player.lower() for player in players]
        self._turnCounter = 0
        self.target = target  # 101, 301, 501, etc
        self.isOver = False

        self.hands = {player: [] for player in self.players}
        self.scores = {player: 0 for player in self.players}

    def scorer(self, player: str, hand: tuple(str)) -> None:
        """
        hand: string of darts, ie 't20 s20 d16'; unless 25 or 50.
        score of hand only added to running total after validation and
        checked for bust
        Assumes valid input.
        """
        self.hands[player].append(hand)
        prevTotal = self.scores[player]
        handScore = 0
        outcome = "SCORE"  # default; mutable
        # iterate through hand
        for i, throw in enumerate(hand):
            if throw in ("25", "50"):
                handScore += int(throw)
            else:
                handScore += self._SCORE_MAP[throw[0]] * int(throw[1:])
        # bust
        if prevTotal + handScore > self.target:
            outcome = "BUST"
        # did not finish on a double
        elif prevTotal + handScore == self.target and (
            hand[-1][0] != "d" and hand[-1][0] != "50"
        ):
            outcome = "BUST"
        # scoring hand
        else:
            self.scores[player] += handScore
            self._turnCounter += 1
            # finish thrown
            # TODO currently major league broken
            if self.scores[player] == self.target and (
                self.hands[player][-1][0] == "d" or self._darts[user][-1] == 50
            ):
                print(f"{user.capitalize()} has won the game!")
                outcome = "FINISH"
                self.gameOver = True
        return outcome

    # TODO
    def _multiplierParser(self, throw: str):
        multi = ""
        # if throw in
        return

    def turnTracker(self) -> str:
        """
        Return: name of the player who must throw.
        """
        return self.players[(self._turnCounter % len(self.players))]

    def exportData(self):
        return

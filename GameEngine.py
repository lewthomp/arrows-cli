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
        self.isOver = False
        self.target = target  # 101, 301, 501, etc

        self._darts = {player: [] for player in self.players}
        self.scores = {player: 0 for player in self.players}
        self._turnCounter = 0

    def scorer(self, player: str, hand: str) -> None:
        """
        hand: string of darts, ie 't20 s20 d16'; unless 25 or 50.
        score of hand only added to running total after validation and
        checked for bust
        Assumes valid input.
        """
        user = player.lower()
        prevTotal = sum(self._scores[user])
        splits = hand.split(" ")
        handScore = 0
        outcome = "SCORE"  # default; mutable
        for i, throw in enumerate(splits):
            multi = throw[0]
            num = int(throw[1:])
            handScore += self._SCORE_MAP[multi] * num
            self._darts[user].append(throw)
        if prevTotal + handScore > self.target:
            outcome = "BUST"
        elif prevTotal + handScore == self.target and self._darts[user][-1][0] != "d":
            outcome = "BUST"
        else:
            self.scores[user] += handScore
            self._turnCounter += 1
            if self.scores[user] == self.target and (
                self._darts[user][-1][0] == "d" or self._darts[user][-1] == 50
            ):
                print(f"{user.capitalize()} has won the game!")
                outcome = "FINISH"
                self.gameOver = True
        return outcome

    def turnTracker(self) -> str:
        """
        Return: name of the player who must throw.
        """
        return self.players[(self._turnCounter % len(self.players))]

    def exportData(self):
        return

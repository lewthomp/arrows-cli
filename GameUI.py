from GameEngine import GameEngine


class GameUI:
    """
    Interface for darts game engine: takes input and reflects
    game state with print statements.
    """

    _MULTI_NAME_MAP = {"s": "single", "d": "double", "t": "treble"}

    def __init__(self, engine: GameEngine):
        self._engine = engine
        self.scores = engine.scores
        self.target = engine.target

    def start(self):
        """
        Loops through players turns
        """
        while True:
            self._scoreboard()
            self._turnHandler()
            # > move advisor
            if self._engine.isOver():
                break
        self._closer()

    def _turnHandler(self):
        player = self._engine.turnTracker()
        remainder = self.target - self.scores[player]
        handInput = input(f"Player {player} has {remainder} remaining.\nenter hand > ")
        print("## HAND INPUT:", type(handInput), handInput)
        validInput = self._validateInput(handInput)
        outcome = self._engine.scorer(player, validInput)
        if outcome == "BUST":
            print(f"Bust! Still {remainder} remaining")
        elif outcome == "SCORE":
            score = self.scores[player][-1]
            print(f"Player {player} scored {score} | {remainder-score} remains.")
        elif outcome == "FINISH":
            finalDart = ""
            print(f"Player {player} hit {finalDart} for a {remainder} finished!")
        else:
            print("## Something has gone very wrong in the turn handler.")

    def _validateInput(self, hand: str, throwNum: int) -> str:
        print("## input received", hand)
        validThrow = False

        throws = hand.split(" ")
        for throw in throws:
            if throw[0] not in ("s", "d", "t"):
                print(
                    f"Throw #{throwNum+1} is invalid: {throw}.\
                    Throw must be prefixed by s, d or t."
                )

        while not validThrow:
            if throw[0] not in ("s", "d", "t"):
                print(
                    f"Throw #{throwNum+1} is invalid: {throw}.\
                    Throw must be prefixed by s, d or t."
                )
            # elif int(throw[1:])
            # check number is valud
            validThrow = True
        #####

    def _closer(self):
        return

    def closer(self):
        self._closer()
        print("Thanks for playing!")

    def _scoreboard(self):
        print()

    def replayer(self):
        choice = input("Play again? [Y/n] > ")
        if choice.lower()[0] in ("n", "N"):
            return False
        return True

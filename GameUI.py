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
        """ """
        throws = hand.split(" ")
        for i, throw in enumerate(throws):
            validThrow = False
            while not validThrow:
                # check prefixed with s/d/t unless number is 25/50
                if throw[0] not in ("s", "d", "t"):
                    if throw not in ("25", "50"):
                        print(
                            f"\nThrow #{i+1} is invalid: {throw}.\
                            Throw must be prefixed by s, d or t."
                        )
                        throw = input(f"\nReenter throw #{i+1}")
                # check number in range (1,..,20)U(25,50)
                elif int(throw[0:]) not in range(1, 21) and throw not in ("25", "50"):
                    print("Invalid score entered as throw #{i}")
                    throw = input(f"\nReenter throw #{i+1}")

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

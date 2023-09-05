class InvalidPlayerCountRange(Exception):
    def __init__(self, total_players: int) -> None:
        self.total_players = total_players
        self.message = "Number of players must be between 1 and 6"
        super().__init__(self.message)


class InvalidPlayerCountType(Exception):
    def __init__(self, total_players: int) -> None:
        self.total_players = total_players
        self.message = "Number of players must an integer"
        super().__init__(self.message)

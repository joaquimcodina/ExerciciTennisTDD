from main.Player import Player


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.__player1 = player1
        self.__player2 = player2

    def won_point(self, player: Player) -> None:
        if player == self.__player1:
            self.__player1.add_points()
        else:
            self.__player2.add_points()
        self.wins_point(player)

    def wins_point(self, player: Player):
        self.__winner = player

    def get_score(self) -> str:
        points_player1 = self.__player1.get_points()
        points_player2 = self.__player2.get_points()

        if points_player1 == 1 and points_player2 == 0:
            return "Fifteen-Love"

        if points_player1 == 2 and points_player2 == 1:
            return "Thirty-Fifteen"

        if points_player1 == 1 and points_player2 == 1:
            return "Fifteen-All"

        return "Love-All"

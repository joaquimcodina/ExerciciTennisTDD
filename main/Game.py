from main.Player import Player

ZERO = ("Love", 0)
FIFTEEN = ("Fifteen", 15)
THIRTY = ("Thirty", 30)
FORTY = ("Forty", 40)

class Game:
    def __init__(self, player1: Player, player2: Player):
        self.__player1 = player1
        self.__player2 = player2
        self.score = [ZERO, FIFTEEN, THIRTY, FORTY]

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
        res = "Love-All"

        if points_player1 <= 3 and points_player2 <= 3:
            if points_player1 == points_player2:
                if points_player1 >= 3 and points_player2 >= 3:
                    return "Deuce"
                else:
                    res = self.score[points_player1][0] + "-All"
            else:
                res = self.score[points_player1][0] + "-" + self.score[points_player2][0]
            return res

        if points_player1 == points_player2 and points_player1 >= 3 and points_player2 >= 3:
            return "Deuce"

        if self.__winner == self.__player1:
            if abs(points_player1 - points_player2) >= 2 and points_player1 >= 4:
                return "Win for player1"
        else:
            if abs(points_player2 - points_player1) >= 2 and points_player2 >= 4:
                return "Win for player2"

        if points_player1 >= 3 and points_player2 >= 3:
            if points_player1 > points_player2:
                return "Advantage player1"
            elif points_player2 > points_player1:
                return "Advantage player2"

        return res

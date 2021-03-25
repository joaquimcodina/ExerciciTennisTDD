class Player:
    def __init__(self, name: str):
        self.__name = name
        self.__num_points = 0

    def add_points(self):
        self.__num_points += 1

    def get_points(self):
        return self.__num_points

    def _eq_(self, player):
        return self.__name == player.__name
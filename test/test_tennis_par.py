import pytest
from main.Game import Game
from main.Player import Player

def create_game(player1: Player, player2: Player):
    return Game(player1, player2)

def create_player(name: str):
    return Player(name)

@pytest.mark.parametrize("score_player_1, score_player_2, expected_result", [
    (0, 0, "Love-All"),
    (1, 0, "Fifteen-Love"),
    (1, 1, "Fifteen-All"),
    (2, 1, "Thirty-Fifteen"),
    (2, 0, "Thirty-Love"),

    (2, 2, "Thirty-All"),
    (3, 3, "Deuce"),
    (4, 4, "Deuce"),
    (0, 1, "Love-Fifteen"),
    (0, 2, "Love-Thirty"),
    (3, 0, "Forty-Love"),
    (0, 3, "Love-Forty"),
    (4, 0, "Win for player1"),
    (0, 4, "Win for player2"),
    (1, 2, "Fifteen-Thirty"),
    (3, 1, "Forty-Fifteen"),
    (1, 3, "Fifteen-Forty"),
    (4, 1, "Win for player1"),
    (1, 4, "Win for player2"),
    (3, 2, "Forty-Thirty"),
    (2, 3, "Thirty-Forty"),
    (4, 2, "Win for player1"),
    (2, 4, "Win for player2"),
    (4, 3, "Advantage player1"),
    (3, 4, "Advantage player2"),
    (5, 4, "Advantage player1"),
    (4, 5, "Advantage player2"),
    (15, 14, "Advantage player1"),
    (14, 15, "Advantage player2"),
    (6, 4, "Win for player1"),
    (4, 6, "Win for player2"),
    (16, 14, "Win for player1"),
    (14, 16, "Win for player2"),
])
def test_game_score(score_player_1: int, score_player_2: int, expected_result: str) -> None:
    #ARRANGE
    player1 = create_player("player1")
    player2 = create_player("player2")
    game = create_game(player1, player2)

    score_max = max(score_player_1, score_player_2)
    for score in range(0, score_max):
        if score < score_player_1:
            game.won_point(player1)
        if score < score_player_2:
            game.won_point(player2)

    #ACT
    result = game.get_score()

    #ASSERT
    assert result == expected_result
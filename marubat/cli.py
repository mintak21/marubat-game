# coding: utf-8
from random import randint
from .ctr import GameController
from .models import Player
from .models import Mark

def main():
    board_size = 3
    board = {(x,y):Mark.NONE for y in range(board_size) for x in range(board_size)}
    player_1 = Player('player1', Mark.MARU)
    player_2 = Player('player2', Mark.BATSU)
    fc = GameController(board, [player_1, player_2])

    fc.game()

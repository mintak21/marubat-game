# coding: utf-8
from random import randint
from .ctr import GameController
from .models import Player
from .models import Mark

def main():
    board_size = 3
    board = {(h,w):Mark.NONE for h in range(board_size) for w in range(board_size)}
    player_1 = Player('player1', Mark.MARU)
    player_2 = Player('player2', Mark.BATSU)
    fc = GameController(board, [player_1, player_2])

    fc.game()

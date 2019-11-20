# coding: utf-8
from .logics import is_bingo
from .logics import bingo_sets
from .logics import mark_filtered_coordinates
from .models import Player
from .models import Mark
from .io import display
from .io import display_board as disp_b

class GameController:
    """進行者

    Attributes
    ------------------------
    board : dict
        ゲームマス(座標:値の辞書、2次元正方行列)
    players : list()
        プレイヤー(2人)

    bingo_sets_cache : set
        ビンゴ可能性座標セット(boardが変わらない限り一緒なのでビンゴ判定キャッシュとして利用)
    turn_player_point : int
        現在のプレイヤーの場所 ポーカー等のボタンのイメージ
    winner : Player
        勝者。ビンゴ判定されたときに設定される
    """

    def __init__(self, board, players):
        self._board = board
        self._bingo_sets_cache = bingo_sets(self._board)
        self._players = players
        self._turn_player_point = 0
        self._winner = None

    def game(self):
        """ゲームを進行する。

        1. ターンプレイヤーにうめる座標を選択させる。
        2. 1のマスにマークを書く。
        3. 終了判定をする。(ビンゴor空きマスなし)
         - 終了条件をみたせば、勝者を宣言してEnd
        4. ターンプレイヤーをスイッチして1に戻る。
        """
        while True:
            disp_b(self._board)

            # 1
            selectables = mark_filtered_coordinates(self._board, Mark.NONE)
            select_coordinate = self._turn_player().select_point(selectables)

            # 2
            self._fill_in(select_coordinate[0], select_coordinate[1], self._turn_player().mark)

            # 3
            if (self._end_game()):
                break
            # 4
            self._switch_player()

        # 結果表示
        disp_b(self._board)
        display(self._turn_player().name + 'の勝ち' if self._winner else '引き分け')

    def _end_game(self):
        """終了判定
        ビンゴ成立 or ブランクマスがない
        ビンゴ成立の場合は、勝者も設定
        """
        if len(mark_filtered_coordinates(self._board, Mark.NONE)) == 0:
            return True
        if is_bingo(self._board, self._turn_player().mark, self._bingo_sets_cache):
            self._winner = self._turn_player
            return True
        return False

    def _fill_in(self, x, y, mark):
        if self._board[x,y] == Mark.NONE:
            self._board[x,y] = mark
        else:
            print('Error') # TODO ロジック上、来ないと思うけれど
            return

    def _switch_player(self):
        self._turn_player_point = (self._turn_player_point + 1) % len(self._players)

    def _turn_player(self):
        return self._players[self._turn_player_point]

# coding: utf-8
from enum import Enum

from .io import select_by_options

class Player:
    """ゲームプレイヤー
    """
    _ask_sentence_fmt = '{name}さん({mark})のターンです。書込座標の番号を入力せよ。(縦方向ポイント,横方向ポイント)、左上マス=(0,0)'

    def __init__(self, name , mark):
        self._name = name
        self._mark = mark

    @property
    def name(self):
        return self._name

    @property
    def mark(self):
        return self._mark

    def select_point(self, selectable):
        # TODO Tactics委譲
        """うめる座標を選択

        Params
        -----------------
        selectable : set
            選択可能座標セット

        Returns
        -----------------
        int,int
            選択した座標
        """
        ask_sentence = Player._ask_sentence_fmt.format(name = self._name, mark = self._mark)
        return select_by_options(selectable, ask_sentence, sort=False)

class Mark(Enum):
    MARU  = '○'
    BATSU = '×'
    NONE  = '-'

    def __str__(self):
        return self.value

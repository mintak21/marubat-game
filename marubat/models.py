# coding: utf-8
from enum import Enum

from .io import select_by_options

class Player:
    """ゲームプレイヤー
    """
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
        return select_by_options(selectable, sort=False)

class Mark(Enum):
    MARU  = '○'
    BATSU = '×'
    NONE  = '-'

    def __str__(self):
        return self.value

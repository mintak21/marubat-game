# coding: utf-8
from math import sqrt

# boardは2次元正方行列であることを前提とする
# 行列同士の演算をするわけではないのでnumpyは使わない

def is_bingo(board, target_mark, cached_bingo_set = None):
    """引数のboardで、ビンゴ成立しているかを判定
    Params
    -----------------
    board : dict
        判定対象ボード(座標:値の辞書、2次元正方行列)
    target_mark : Mark
        判定するマーク

    Returns
    -----------------
    bool
        ビンゴであればTrue、そうでなければFalse
    """
    target_mark_coordinates = set(mark_filtered_coordinates(board, target_mark))
    bingo_set_list = bingo_sets(board) if cached_bingo_set else cached_bingo_set
    for bingo_set in bingo_set_list:
        if target_mark_coordinates == bingo_set:
            return True
    return False

def mark_filtered_coordinates(board, target_mark, how_to= 'row'):
    """引数のマークを持つ座標のリストを取得

    Params
    -----------------
    board : dict
        判定対象ボード(座標:値の辞書、2次元正方行列)
    target_mark : Mark
        判定するマーク
    how_to : string (default=row)
        ソート方法
        row -> 横方向->縦方向 [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)...]
        col -> 縦方向->横方向 [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2)...]

    Returns
    -----------------
    list
        判定マークの入っている座標リスト
    """
    target_coordinates = [
        coordinate for coordinate, mark in board.items() if mark == target_mark
    ]
    if how_to == 'row':
        return sorted(target_coordinates, key=lambda v : v[0])
    elif how_to == 'col':
        return sorted(target_coordinates, key=lambda v : v[1])
    else:
        return sorted(target_coordinates) #default sort

def bingo_sets(board):
    """ビンゴとなる座標セットを取得
    ex. 3*3 n=3の場合
    result =[{(0,0),(0,1),(0,2)},{(1,0),(1,1),(1,2)},{(2,0),(2,1),(2,2)}, よこ
             {(0,0),(1,0),(2,0)},{(0,1),(1,1),(2,1)},{(0,2),(1,2),(2,2)}, たて
             {(0,2),(1,1),(2,0)}, ななめ(右上方向)
             {(0,0),(1,1),(2,2)}, ななめ(右下方向)
    ]
    Params
    -----------------
    board : dict
        判定対象ボード(座標:値の辞書、2次元正方行列)

    Returns
    -----------------
    list
        ビンゴとなる座標セットリスト
    """
    result = list()
    board_size = _board_size(board)
    # よこ
    for w in range(board_size):
        result.append({(h, w) for h in range(board_size)})
    # たて
    for h in range(board_size):
        result.append({(h, w) for w in range(board_size)})
    # ななめ(右上)
    result.append({(k, board_size-(k+1)) for k in range(board_size)})
    # ななめ(右下)
    result.append({(k, k) for k in range(board_size)})

    return result

def _board_size(board):
    return int(sqrt(len(board)))

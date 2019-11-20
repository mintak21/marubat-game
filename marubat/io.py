# coding: utf-8
import os
from math import sqrt

def select_by_options(options, ask_sentence = '選択肢の番号を入力してください。', sort = True):
    """選択肢を表示して標準入力より選択させる。

    Parameters
    ------------------
    options : Iterable
        選択肢一覧
    ask_sentence : string
        問いかけ文
    sort : bool
        optionsをソートした状態とするかどうか

    Returns
    ------------------
    object : options[any]
        optionsより選択した結果
    """
    target = sorted(options) if sort else options
    option_str = '  '.join(
            [str(num) + ' :' + str(value) for num, value in enumerate(target)]
        )
    sentence = os.linesep.join([ask_sentence, option_str, '>'])
    # TODO 変換&OutRangeエラーハンドリング
    input_str = input(sentence)
    input_num = int(input_str)
    return list(target)[input_num]

def display_board(board, separator = '|'):
    """座標、値の辞書をセパレータで区切って以下のように表示する。
    ex |1|2|3|
       |4|5|6|
       |7|8|9|

    Parameters
    ------------------
    board : dict
        座標、値の辞書
    separator : string
        区切り文字 default = |
    """
    result = separator.join([str(v) if k[0] != int(sqrt(len(board))) - 1 else \
                            str(v) + '|' + os.linesep for k,v in board.items()])
    display('【ボード】', '|' + result.rstrip())

def display(*disp_sentence):
    """受け取ったものをそのまま標準出力。
    複数指定された場合は、改行して出力する。
    """
    print(os.linesep.join(list(map(str, disp_sentence))))

# coding: utf-8
import os

def select_by_options(options, ask_sentence = '選択肢の番号を入力してください。', sort = True):
    """選択肢を表示して標準入力より選択させる。

    Parameters
    ------------------
    options : Iterable
        選択肢一覧
    ask_sentence : string
        問いかけ文

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

def display(disp_sentence):
    print(disp_sentence)

# coding: utf-8
import copy as c
import marubat.logics as l
from marubat.models import Mark

class TestTools(object):
    def test_is_bingo_3_3(self):
        assert l.is_bingo(self.three_maru_row_bingo, Mark.MARU)
        assert l.is_bingo(self.three_batsu_col_bingo, Mark.BATSU)
        assert l.is_bingo(self.three_batsu_slant_bingo, Mark.BATSU)
        assert l.is_bingo(self.three_all_non_bingo, Mark.MARU) is False
        assert l.is_bingo(self.three_all_non_bingo, Mark.MARU) is False

    def test_mark_filtered_coordinates_3_3(self):
        expected_maru = [(0,0), (1,1), (1,2)]
        expected_batsu = [(0,1), (0,2), (1,0), (2,1), (2,2)]
        expected_blank = [(2,0)]
        actual_maru = l.mark_filtered_coordinates(self.three_all_non_bingo, Mark.MARU)
        actual_batsu = l.mark_filtered_coordinates(self.three_all_non_bingo, Mark.BATSU)
        actual_blank = l.mark_filtered_coordinates(self.three_all_non_bingo, Mark.NONE)

        assert expected_maru == actual_maru
        assert expected_batsu == actual_batsu
        assert expected_blank == actual_blank

    def test_mark_filtered_coordinates_5_5(self):
        pass

    def test_bingo_sets_3_3(self):
        expected_three = [
            # たて
            {(0,0), (1,0), (2,0)},
            {(0,1), (1,1), (2,1)},
            {(0,2), (1,2), (2,2)},
            # よこ
            {(0,0), (0,1), (0,2)},
            {(1,0), (1,1), (1,2)},
            {(2,0), (2,1), (2,2)},
            # ななめ
            {(0,2), (1,1), (2,0)},
            {(0,0), (1,1), (2,2)},
        ]
        actual_three = l.bingo_sets(self.three_blank)
        assert len(expected_three) == len(actual_three)
        for i in range(len(expected_three)):
            assert expected_three[i] == actual_three[i]

    def test_bingo_sets_5_5(self):
        expected_five = [
            # たて
            {(0,0), (1,0), (2,0), (3,0), (4,0)},
            {(0,1), (1,1), (2,1), (3,1), (4,1)},
            {(0,2), (1,2), (2,2), (3,2), (4,2)},
            {(0,3), (1,3), (2,3), (3,3), (4,3)},
            {(0,4), (1,4), (2,4), (3,4), (4,4)},
            # よこ
            {(0,0), (0,1), (0,2), (0,3), (0,4)},
            {(1,0), (1,1), (1,2), (1,3), (1,4)},
            {(2,0), (2,1), (2,2), (2,3), (2,4)},
            {(3,0), (3,1), (3,2), (3,3), (3,4)},
            {(4,0), (4,1), (4,2), (4,3), (4,4)},
            # ななめ
            {(0,4), (1,3), (2,2), (3,1), (4,0)},
            {(0,0), (1,1), (2,2), (3,3), (4,4)},
        ]
        actual_five = l.bingo_sets(self.five_blank)
        assert len(expected_five) == len(actual_five)
        for i in range(len(expected_five)):
            assert expected_five[i] == actual_five[i]

    def setup_method(self, method):
        # 3*3マス
        self.three_blank = {(x,y):Mark.NONE for y in range(3) for x in range(3)}
        # 5*5マス
        self.five_blank = {(x,y):Mark.NONE for y in range(5) for x in range(5)}
        ''' 3*3 All Non Bingo
        |○|×|×|
        |×|○|○|
        |-|×|×|
        '''
        self.three_all_non_bingo = c.deepcopy(self.three_blank)
        self.three_all_non_bingo[0, 0] = Mark.MARU
        self.three_all_non_bingo[1, 1] = Mark.MARU
        self.three_all_non_bingo[1, 2] = Mark.MARU
        self.three_all_non_bingo[0, 1] = Mark.BATSU
        self.three_all_non_bingo[0, 2] = Mark.BATSU
        self.three_all_non_bingo[1, 0] = Mark.BATSU
        self.three_all_non_bingo[2, 1] = Mark.BATSU
        self.three_all_non_bingo[2, 2] = Mark.BATSU
        ''' 3*3 Batsu Bingo col
        |○|×|×|
        |○|○|×|
        |-|-|×|
        '''
        self.three_batsu_col_bingo = c.deepcopy(self.three_blank)
        self.three_batsu_col_bingo[0, 0] = Mark.MARU
        self.three_batsu_col_bingo[1, 0] = Mark.MARU
        self.three_batsu_col_bingo[1, 1] = Mark.MARU
        self.three_batsu_col_bingo[0, 1] = Mark.BATSU
        self.three_batsu_col_bingo[0, 2] = Mark.BATSU
        self.three_batsu_col_bingo[1, 2] = Mark.BATSU
        self.three_batsu_col_bingo[2, 2] = Mark.BATSU
        ''' 3*3 Maru Bingo row
        |○|×|×|
        |○|○|○|
        |-|-|×|
        '''
        self.three_maru_row_bingo = c.deepcopy(self.three_blank)
        self.three_maru_row_bingo[0, 0] = Mark.MARU
        self.three_maru_row_bingo[1, 0] = Mark.MARU
        self.three_maru_row_bingo[1, 1] = Mark.MARU
        self.three_maru_row_bingo[1, 2] = Mark.MARU
        self.three_maru_row_bingo[0, 1] = Mark.BATSU
        self.three_maru_row_bingo[0, 2] = Mark.BATSU
        self.three_maru_row_bingo[2, 2] = Mark.BATSU
        ''' 3*3 Batsu Bingo slant
        |○|○|×|
        |○|×|○|
        |×|○|×|
        '''
        self.three_batsu_slant_bingo = c.deepcopy(self.three_blank)
        self.three_batsu_slant_bingo[0, 0] = Mark.MARU
        self.three_batsu_slant_bingo[0, 1] = Mark.MARU
        self.three_batsu_slant_bingo[1, 0] = Mark.MARU
        self.three_batsu_slant_bingo[1, 2] = Mark.MARU
        self.three_batsu_slant_bingo[2, 1] = Mark.MARU
        self.three_batsu_slant_bingo[0, 2] = Mark.BATSU
        self.three_batsu_slant_bingo[1, 1] = Mark.BATSU
        self.three_batsu_slant_bingo[2, 0] = Mark.BATSU
        self.three_batsu_slant_bingo[2, 2] = Mark.BATSU


    def teardown_method(self, method):
        pass

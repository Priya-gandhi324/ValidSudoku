import unittest
from ValidSudoku import isValidSudoku

class TestSum(unittest.TestCase):
    def test_for_valid(self):
        data = [[[7, 9, 2, 1, 5, 4, 3, 8, 6], 
                [6, 4, 3, 8, 2, 7, 1, 5, 9],
                [8, 5, 1, 3, 9, 6, 7, 2, 4],
                [2, 6, 5, 9, 7, 3, 8, 4, 1],
                [4, 8, 9, 5, 6, 1, 2, 7, 3],
                [3, 1, 7, 4, 8, 2, 9, 6, 5],
                [1, 3, 6, 7, 4, 8, 5, 9, 2],
                [9, 7, 4, 2, 1, 5, 6, 3, 8],
                [5, 2, 8, 6, 3, 9, 4, 1, 7]],
                [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]]
        for test_case in data:
            result = isValidSudoku(test_case)
            self.assertEqual(result, True)
    
    def test_for_invalid(self):
        data = [[5, 5, 5, 5, 5, 5, 5, 5, 5], 
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5, 5, 5, 5, 5]]
        result = isValidSudoku(data)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
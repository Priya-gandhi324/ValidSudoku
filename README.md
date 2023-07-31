# ValidSudoku
This is a simple Python program that checks whether a given Sudoku board is valid or not using Hashset. The Sudoku board is a 9x9 grid, where each cell can contain a digit from 1 to 9, or a blank space represented by 0 or '.'.

# Input Format
The Sudoku board should be provided as a list of lists, where each inner list represents a row of the board. The digits and blank spaces should be represented as integers (0-9) or strings (using '.' for blank spaces).

Here's an example:
'''python
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
'''

# Running the Program
To check if a Sudoku board is valid, you can use the isValidSudoku function from the ValidSudoku.py module.

# Tests
I have provided some test cases in the tests.py file to verify the correctness of the is_valid_sudoku function. To run the tests, execute the following command in your terminal:
'''python 
python tests.py 
'''

The output will show whether each test case passes or fails.

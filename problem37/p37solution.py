"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the
    9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Example 1:
    Input:
        board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"],
        ]
        Output: [
            ["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","9"],
        ]

Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution
"""

import pprint
from typing import List


SUDOKU_VALUES = "123456789"
NUM_SUDOKU_VALUES = len(SUDOKU_VALUES)
NUM_COLS = 9
NUM_ROWS = 9


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # This implementation avoids using Python build in types, such as
        # sets, that may not be available in other languages. Also, in my
        # tests the boolean mask solution was a bit faster than the set
        # solution, but the difference was so small that maybe in other
        # system's or python versions the result is the opposite.

        # Bool mask for each value 1 to 9, set to True if the value is
        # already present on the row/col/box.
        row_values = [[False] * NUM_SUDOKU_VALUES for _ in range(NUM_COLS)]
        col_values = [[False] * NUM_SUDOKU_VALUES for _ in range(NUM_COLS)]
        box_values = [[[False] * NUM_SUDOKU_VALUES for _ in range(3)] for _ in range(3)]

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if board[i][j] != ".":
                    v_index = int(board[i][j], 10) - 1
                    row_values[i][v_index] = True
                    col_values[j][v_index] = True
                    box_values[i // 3][j // 3][v_index] = True

        # Count number of missing values per cell
        missing_values_count = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                if board[i][j] == ".":
                    # mask = [
                    #    any(m)
                    #     for m in zip(
                    #         row_values[i], col_values[j], box_values[i // 3][j // 3]
                    #     )
                    # ]
                    mask = map(
                        any,
                        zip(row_values[i], col_values[j], box_values[i // 3][j // 3]),
                    )
                    missing_values_count[i][j] = NUM_SUDOKU_VALUES - sum(mask)

        # Generate list of "empty cells" and sort it by missing value
        to_fill = [
            (i, j)
            for i in range(NUM_ROWS)
            for j in range(NUM_COLS)
            if board[i][j] == "."
        ]
        to_fill.sort(key=lambda cell: missing_values_count[cell[0]][cell[1]])

        # Recursive search
        def _search_solution(index: int) -> bool:
            if index >= len(to_fill):
                return True

            row, col = to_fill[index]
            box_i = row // 3
            box_j = col // 3
            for v_index, v in enumerate(SUDOKU_VALUES):
                if (
                    row_values[row][v_index]
                    or col_values[col][v_index]
                    or box_values[box_i][box_j][v_index]
                ):
                    continue

                board[row][col] = v
                row_values[row][v_index] = True
                col_values[col][v_index] = True
                box_values[box_i][box_j][v_index] = True

                if _search_solution(index + 1):
                    return True

                row_values[row][v_index] = False
                col_values[col][v_index] = False
                box_values[box_i][box_j][v_index] = False

            return False

        _search_solution(0)


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    # This one causes time limit with naive solution
    # Times in MacBook pro 2022
    # Naive: 2.59 - 2.68 second
    board = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "9", ".", ".", "1", ".", ".", "3", "."],
        [".", ".", "6", ".", "2", ".", "7", ".", "."],
        [".", ".", ".", "3", ".", "4", ".", ".", "."],
        ["2", "1", ".", ".", ".", ".", ".", "9", "8"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "2", "5", ".", "6", "4", ".", "."],
        [".", "8", ".", ".", ".", ".", ".", "1", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]

    solution = Solution()
    solution.solveSudoku(board)

    pprint.pprint(board)

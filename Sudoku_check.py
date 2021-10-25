def done_or_not(board):  # board[i][j]
    # your solution here
    board_rotated = []
    for i in range(9):
        col = []
        for j in range(9):
            col.append(board[j][i])
        board_rotated.append(col)

    subboards = subboard_3x3(board)

    if rows_check(board_rotated) and rows_check(board) and rows_check(subboards):
        return 'Finished!'
    else:
        return 'Try again!'


def rows_check(board):
    for row in board:
        if len(set(row)) != len(row):
            return False
    return True

def subboard_3x3(board):
    subboard_3x3 = []
    for el1 in [0, 3, 6]:
        for el in [0, 3, 6]:
            col = []
            for i in range(el1, el1 + 3):
                for j in range(el, el + 3):
                    col.append(board[i][j])
            subboard_3x3.append(col)
    return subboard_3x3

print(
done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                               ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                               ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                               ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                               ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                               ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                               ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                               ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                               ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])
)

print(
done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])
)

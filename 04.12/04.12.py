
# Input handeling
from abc import abstractproperty

with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/04.12/input.in") as fin:
    number_calls, *boards = fin.read().split('\n\n')
    number_calls = [int(i) for i in number_calls.split(',')]
    #boards = fin.read().strip().split('\n')
    boards = [[[int(col) for col in row.split()] for row in board.split('\n') ] for board in boards ]


# Marking the board function
def mark_board(number_called, board):
    for row in board:
        for col in range(0, len(row)):
            if row[col] == number_called:
                row[col] = -1

# Adding the remainder of the board
def add_board(board):
    count = 0
    for row in board:
        for col in row:
            if col != -1:
                count += col
    return count

# Check for winner
def win_check(board):

    won = False
    for row in board:
        won = all(elem in [-1] for elem in row)

        if won:
            return won

    for col in range(0, 5):
        won = all(elem in [-1] for elem in [row[col] for row in board])

        if won:
            return won

    return won

def part1():
    for num in number_calls:
        for board in boards:
            mark_board(num, board)

            if win_check(board):
                return add_board(board) * num

"""
def part2():
    
    Try to find the last board that will win, and then sum the rest of it
    last_board = False
    boards_won = 0

    while last_board is False:
        for num in number_calls:
            for board in boards: 
                mark_board(num, board)

                if win_check(board):
                    boards_won += 1

                if boards_won == boards:
                    return add_board(board) * num
"""
ans = part1
print(ans)
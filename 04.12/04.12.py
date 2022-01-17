
# Input handeling

with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/04.12/input.in") as fin:
    number_calls, *boards = fin.read().split('\n\n')
    number_calls = [int(i) for i in number_calls.split(',')]
    #boards = fin.read().strip().split('\n')
    allboards = [[[int(col) for col in row.split()] for row in board.split('\n') ] for board in boards ]


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
    print(number_calls)
    for num in number_calls:
        for board in boards:
            mark_board(num, board)

            if win_check(board):
                return add_board(board) * num

def part2(number_calls, allboards):
    last_board = False
    numbers = number_calls
    boards = allboards

    while not last_board:
        number = numbers[0]
        numbers = numbers[1:]

        for board in boards:
            mark_board(number, board)
        
        index = 0
        while index < len(boards):
            if win_check(boards[index]):
                if len(boards) > 1:
                    boards.pop(index)
                
                else:
                    last_board = True
                    return add_board(boards[index]) * number
            
            else:
                index += 1

ans = part2(number_calls, allboards)
print(ans)
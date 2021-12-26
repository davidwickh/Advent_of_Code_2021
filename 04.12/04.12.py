
# Input handeling
from abc import abstractproperty

with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/04.12/input.in") as fin:
    number_calls = fin.readline()
    boards = fin.read().strip().split( '\n')

# Splitting boards into dictionary
boards_new = []
boards_dict = {}
for row in boards:
    if row != '':
        boards_new.append([row])

h = 5    
count = 0
board_num = 0
for row in boards_new:
    if count == 0:
        boards_dict['board: ' + str(board_num)] = row
    elif count < h and not 0:
        boards_dict['board: ' + str(board_num)].append(row)
    count +=1
    if count == h:
        count = 0
        board_num += 1


# Numbers that are called function
def nums_called(num_list, turn):
    int(num_list)
    nums_called = num_list[:turn]
    return nums_called


# Checking a board for a win function
def check_win(dictionary=None):
    for board_num in dictionary:
        board = dictionary[board_num]
        


    pass

#check_win(boards_dict)

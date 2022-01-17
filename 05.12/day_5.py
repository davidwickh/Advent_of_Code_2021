# Data input and handelling
with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/05.12/input.in") as fin:
    data = fin.read().strip().split('\n')
    data = [int(i) for i in data.split(' -> ')]
    

    #allboards = [[[int(col) for col in row.split()] for row in board.split('\n') ] for board in boards ]


print(data)
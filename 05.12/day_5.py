# Data input and handling
with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/05.12/input.in") as fin:
    data = fin.read().strip()
    data = [x.split(' -> ') for x in data.split('\n')]


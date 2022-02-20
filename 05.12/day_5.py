import numpy as np
import re

# Data input and handling
with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/05.12/input.in") as fin:
    data = fin.read().strip()
    data = re.split(' -> |, |\n', data)
    data = [x.split(',') for x in data]
    
# Data is in format
#[
# [x1, y1], [x2, y2], 
#   [x1, y1], [x2, y2], ...
# ]

# Create a zeros 2 x 2 vector the size of the field
max_num = int(max(map(max, data)))    # Finding the max number in data set
field = np.zeros((max_num, max_num), dtype=int)

# Splitting the data into a list of x values and y values
x_lst=[]
y_lst=[]
for row in data:
    x = row[0]
    y = row[1]
    x_lst.append(x)
    y_lst.append(y)

# Splitting the x and y lists into lists of x1, x2 and y1, y2 values
x1_lst = []
x2_lst = []
count = 0
for row in x_lst:
    x = row
    if count == 0:
        x1_lst.append(x)
        count += 1
        continue
    if count == 1:
        x2_lst.append(x)
        count -= 1
        continue
y1_lst = []
y2_lst = []
count = 0
for row in y_lst:
    y = row
    if count == 0:
        y1_lst.append(y)
        count += 1
        continue
    if count == 1:
        y2_lst.append(y)
        count -= 1
        continue

for r in range(len(y1_lst)):
    if y1_lst[r] == y2_lst[r] or x1_lst[r] == x2_lst[r]:
        y1 = y1_lst[r]
        y2 = y2_lst[r]
        x1 = x1_lst[r]
        x2 = x2_lst[r]
        
        
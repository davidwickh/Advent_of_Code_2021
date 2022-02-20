import numpy as np

# Data input and handling
with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/05.12/input.in") as fin:
    data = fin.read().strip()
    data = [x.split(',') for x in data.split('\n')]
    
    
    # data = [[int(float(x.replace(',', ''))) for x in y] for y in data]
for x in data:
   print(x)

# Data is in format
#[
# [x1, y1], [x2, y2], 
#   [x1, y1], [x2, y2], ...
# ]


# # Create a zeros 2 x 2 vector the size of the field
# max_num = int(max(map(max, data)))    # Finding the max number in data set
# field = np.zeros((max_num, max_num), dtype=int)

# x_lst=[]
# y_lst=[]
# for row in data:
#     x = row[0]
#     y = row[1]
    
#     x_lst.append(x)
#     y_lst.append(y)

# x1_lst = []
# x2_lst = []
# count = 0
# for row in x_lst:
#     x = row
#     if count == 0:
#         x1_lst.append(x)
#         count += 1
#         continue
#     if count == 1:
#         x2_lst.append(x)
#         count -= 1
#         continue

# y1_lst = []
# y2_lst = []
# count = 0
# for row in y_lst:
#     y = row
#     if count == 0:
#         y1_lst.append(y)
#         count += 1
#         continue
#     if count == 1:
#         y2_lst.append(y)
#         count -= 1
#         continue



# for r in range(len(y1_lst)):
#     if y1_lst[r] == y2_lst[r] or x1_lst[r] == x2_lst[r]:
#         print('y:' + str(y1_lst[r]) + ',' + str(y2_lst[r]) + '\n' + 'x:' + str(x1_lst[r]) + ',' + str(x2_lst[r]) + '\n\n')
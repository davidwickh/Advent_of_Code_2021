import numpy as np
import re


def part_1():
    # Data input and handling
    with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/05.12/input.in") as fin:
        data = fin.read().strip()
        data = re.split(' -> |, |\n', data)
        data = [x.split(',') for x in data]

    # Data is in format
    # [
    # [x1, y1],
    # [x2, y2],
    # [x1, y1],
    # [x2, y2], ...
    # ]

    x_1_lst = []
    x_2_lst = []
    y_1_lst = []
    y_2_lst = []

    count = 0
    for coordinate in data:
        try:
            coordinate_1 = data[count]
            coordinate_2 = data[count + 1]
            x_1 = int(coordinate_1[0])
            y_1 = int(coordinate_1[1])
            x_2 = int(coordinate_2[0])
            y_2 = int(coordinate_2[1])

            # Check if x_1 and x_2 or y_1 and y_2 are the same
            if x_1 == x_2 or y_1 == y_2:
                x_1_lst.append(x_1)
                x_2_lst.append(x_2)
                y_1_lst.append(y_1)
                y_2_lst.append(y_2)

            count += 2
        except IndexError:
            count += 1

    # get the max x and y values
    x_1_max = max(x_1_lst)
    x_2_max = max(x_2_lst)
    y_1_max = max(y_1_lst)
    y_2_max = max(y_2_lst)
    x_max = max(x_1_max, x_2_max)
    y_max = max(y_1_max, y_2_max)

    # create a matrix of zeros
    matrix = np.zeros((x_max + 1, y_max + 1))

    # Loop through x and y values and set the matrix to 1
    for i in range(len(x_1_lst)):
        x_1 = x_1_lst[i]
        x_2 = x_2_lst[i]
        y_1 = y_1_lst[i]
        y_2 = y_2_lst[i]
        x_1_new = min(x_1, x_2)
        x_2_new = max(x_1, x_2)
        y_1_new = min(y_1, y_2)
        y_2_new = max(y_1, y_2)
        if x_1_new == x_2_new:
            matrix[x_1_new, y_1_new:y_2_new + 1] += 1
        elif y_1_new == y_2_new:
            matrix[x_1_new:x_2_new + 1, y_1_new] += 1
        # matrix[9:3, 4] += 1

    # count how many positions have a value of 2 or more in the matrix
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] >= 2:
                count += 1

    print(count)


if __name__ == "__main__":
    part_1()

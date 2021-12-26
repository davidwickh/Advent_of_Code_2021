#Input handeling
from typing import _ProtocolMeta


with open("/Users/David/Documents/GitHub/Advent_of_Code_2021/03.12/input.in") as fin:
    data = [i for i in fin.read().strip().split("\n")]

def most_common(input=None):
    common_count = []
    least_common_count = []
    for column in range(0, len(data[0])):
        zeros = 0
        ones = 0
        for bitString in data:
            if bitString[column] == '0':
                zeros += 1
            else:
                ones += 1
    
        if zeros > ones:
            common_count.append('0')
            least_common_count.append('1')
        elif zeros < ones: 
            common_count.append('1')
            least_common_count.append('0')
    
    common_count = ''.join(common_count)
    least_common_count = ''.join(least_common_count)
    common_dec = int(common_bin, 2)
    least_common_dec = int(least_common_bin, 2)

    part_1_ans = common_dec * least_common_dec
    
    return part_1_ans



#Part 2 - life support rating

def part_2(input=None):
    O2_data = data.copy()
    # Oxygen generator rating
    i = 0
    while len(O2_data) > 1:
        ones = 0
        zeros = 0

        for bitString in O2_data:
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1
        
        # List shortener
        if zeros > ones:
            O2_data = [bitString for bitString in O2_data if bitString[i] == '0' ]
        else:
            O2_data = [bitString for bitString in O2_data if bitString[i] == '1' ]

        i += 1
    O2_rating = ''.join(O2_data)

    # CO2 scrubber rating
    CO2_data = data.copy()
    i = 0
    while len(CO2_data) > 1:
        zeros = 0
        ones = 0

        # Counter
        for bitString in CO2_data:
            if bitString[i] == '0':
                zeros += 1
            else:
                ones += 1
        
        # List shortener
        if zeros > ones:
            CO2_data = [bitString for bitString in CO2_data if bitString[i] == '1' ]
        else:
            CO2_data = [bitString for bitString in CO2_data if bitString[i] == '0' ]

        i += 1

    CO2_rating = ''.join(CO2_data)

    lifesupport_rating = int(O2_rating, 2) * int(CO2_rating, 2)
    
    return lifesupport_rating

print(part_2(data))
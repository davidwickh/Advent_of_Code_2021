import numpy as np
import pandas as pd


def count_increase():
    """
    Takes the input csv file and compares 
    """
    df = pd.read_csv("/Users/David/Documents/GitHub/Advent_of_Code_2021/02.12/Input.csv")
    three_measurement = []
    results = []


    for row, value in df.iterrows():
        if row < (len(df.index) -2):
            current_three_sum = df.iloc[row].value + df.iloc[row + 1].value + df.iloc[row + 2].value
            three_measurement.append(current_three_sum) 
        
    for r in range(len(three_measurement)-1):
        if three_measurement[r + 1] > three_measurement[r]:
            results.append("increased")
    
    increases = results.count("increased")
    print(increases)
    


if __name__ == "__main__":
    count_increase()

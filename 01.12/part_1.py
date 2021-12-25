from os import name
from typing import ValuesView
import numpy as np
import pandas as pd


def count_increase():
    """
    Takes the input csv file and compares 
    """
    df = pd.read_csv("/Users/David/Documents/GitHub/Advent_of_Code_2021/01.12/Input.csv")
    results = []

    for row, value in df.iterrows():
        if df.iloc[row].value > df.iloc[row - 1].value:
            results.append("increased")
        else:
            results.append("decreased")

    increases = results.count('increased')

    print(increases)

if __name__ == "__main__":
    count_increase()

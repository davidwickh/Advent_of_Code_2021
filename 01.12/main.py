import numpy as np
import pandas as pd


def count_increase():
    df = pd.read_csv("Input.csv")
    results = []

    for row in df.rows:
        if r == 0:
            continue
        results.append(df.iloc[r])
    print(results)


if __name__ == '__main__':
    count_increase()
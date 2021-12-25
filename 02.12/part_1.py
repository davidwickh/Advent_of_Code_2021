import numpy as np
import pandas as pd

def directions():
    df = pd.read_csv("/Users/David/Documents/GitHub/Advent_of_Code_2021/02.12/Input.csv", delimiter=" ")

    horz_pos = 0
    depth_pos = 0

    for dir, unit in df.itertuples(index=False):
        hor_ops = {
            "forward": horz_pos + unit,
            "backward": horz_pos - unit,
        }
        depth_ops = {
            "down": depth_pos + unit,
            "up": depth_pos - unit
        } 
        
        horz_pos = hor_ops.get(dir, horz_pos)
        depth_pos = depth_ops.get(dir, depth_pos)

    print(horz_pos, depth_pos)

    result = horz_pos * depth_pos
    print(result)
        


if __name__ == "__main__":
    directions()
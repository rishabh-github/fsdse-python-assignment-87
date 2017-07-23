import pandas as pd

def solution(array):
    ds = pd.Series(array)
    return ds

print solution([2, 4, 6, 8, 10])

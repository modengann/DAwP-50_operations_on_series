#!/usr/bin/env python3

import pandas as pd

def create_series(L1, L2):
    pass
    
def modify_series(s1, s2):
    pass
    
def main():
    series = create_series([1,2,3], [10, 20, 30])
    result = modify_series(series[0], series[1])
    haha = result[0].add(result[1])
    haha2 = result[0] + result[1]
    print(haha2)
    print(result[0].values)
    print(result[1].values)

if __name__ == "__main__":
    main()

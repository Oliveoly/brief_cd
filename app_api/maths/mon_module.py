import pandas as pd


def add(a: int,b:int) -> int:
    return a+b

def sub(a:int,b:int) ->int :
    return a -b

def square(a:int) ->int :
    return a*a

def print_data(df :pd.DataFrame) -> int :
    print(df)
    return df.count()

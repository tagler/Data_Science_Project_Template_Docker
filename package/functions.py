import pandas as pd # type: ignore

from typing import List

def add(x: int, y: int) -> int:
    """
    Function that adds two values
    """
    return x + y

def sub(x: int, y: int) -> int:
    """
    Function that subtracts two values
    """
    return x - y

def create_df(a: List[int], b: List[int]) -> pd.DataFrame:
    """
    Create dataframe
    """
    df: pd.DataFrame = pd.DataFrame(
        {
        "A" : a,
        "B" : b,
        }
    )
    return df
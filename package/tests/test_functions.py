import pytest

# relative import 
# NOTE: run via cmd: pytest package/tests/ (in project root dir)
from .. import functions

# alternate import 
# NOTE: run via cmd: pytest . (in tests dir)
#import sys
#sys.path.append("..")
#import functions 

import pandas as pd

from typing import List

def test_add():
    input_x: int = 2
    input_y: int = 2
    output: int = 4
    actual = functions.add(input_x, input_y)
    assert output == actual 
    
def test_sub():
    input_x: int = 10
    input_y: int = 5
    output: int = 5
    actual = functions.sub(input_x, input_y)
    assert output == actual 

def test_add_type():
    input_x: int = 10
    input_y: int = 5
    actual = functions.sub(input_x, input_y)
    assert isinstance(actual, int)

def test_create_df():
    input_a: List[int] = [1,2,3]
    input_b: List[int] = [4,5,6]
    output: pd.DataFrame = pd.DataFrame(
        {
        "A" : [1,2,3],
        "B" : [4,5,6],
        }
    )
    actual = functions.create_df(input_a, input_b)
    assert pd.DataFrame.equals(output, actual)
import pytest

import script 

def test_sum():
    input_x: int = 1
    input_y: int = 2
    input_z: int = 3
    output: int = 6
    actual = script.sum(input_x, input_y, input_z)
    assert output == actual 
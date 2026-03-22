import numpy as np
import pandas as pd
import pytest

from app_api.maths.mon_module import add, print_data, square, sub


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 12),
    (20, 2, 22),
    (0, 2, 2),
])
def test_add(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 8),
    (20, 2, 18),
    (0, 2, -2),
])
def test_sub(a: int, b: int, expected: int) -> None:
    assert sub(a, b) == expected

@pytest.mark.parametrize("a,expected", [
    (10,100),
    (-1,1),
    (0, 0),
])
def test_square(a: int, expected: int) -> None:
    assert square(a) == expected


input_df = pd.DataFrame(data=np.random.randint(1,10,(5,3)), columns =["col1","col2","col3"])

@pytest.fixture(scope="module", params=input_df)
def test_print_df(request) :
    assert print_data(request.param) == 5

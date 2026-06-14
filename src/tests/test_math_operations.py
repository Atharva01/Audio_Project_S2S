import pytest
from src.math_operations import add, mul
import logging

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("x,y",[
    (2,3),
    (10, 5)
])

def test_add(x,y):
    result = add(x,y)
    assert isinstance(result,int),f"Expected int, but got {type(result).__name__}"


@pytest.mark.parametrize("x, y", [
    (4, 2),
    (0, 9),
])

def test_mul(x, y):
    # Note: Corrected function name spelling from test_muk to test_mul
    result = mul(x, y)
    assert isinstance(result, int), f"Expected int, but got {type(result).__name__}"
import pytest
from api import calculate_prize_amount


TEST_DATA = [(100, "1/2", 50),
             (100, "1/3", 33.33),
             (0, "1/4", 0),
             (100, "1/1", 100),
             (100, "1/100", 1)]


@pytest.mark.parametrize("prize_amount, portion_str, expected", TEST_DATA)
def test_calculate_prize_amount(prize_amount: int, portion_str: str, expected: float):
    assert calculate_prize_amount(prize_amount, portion_str) == pytest.approx(expected, 0.001)

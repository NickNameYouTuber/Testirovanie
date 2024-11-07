import pytest

def calculate_area(length: float, width: float) -> float:
    return length * width

@pytest.mark.parametrize("length, width, expected", [
    (2, 3, 6),
    (0, 5, 0),
    (4, 0, 0),
    (1.5, 2.5, 3.75),
    (-3, 2, -6),
])
def test_calculate_area(length, width, expected):
    assert calculate_area(length, width) == expected
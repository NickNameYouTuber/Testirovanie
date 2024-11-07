import pytest

def is_even(number: int) -> bool:
    return number % 2 == 0

# Параметризованный тест
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
    (-7, False),
])
def test_is_even(number, expected):
    assert is_even(number) == expected
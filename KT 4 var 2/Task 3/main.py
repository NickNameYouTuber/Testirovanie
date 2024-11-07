import pytest

def classify_triangle(a: float, b: float, c: float) -> str:
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 3, 3, "равносторонний"),
    (3, 3, 4, "равнобедренный"),
    (3, 4, 5, "разносторонний"),
    (5, 5, 5, "равносторонний"),
    (4, 4, 6, "равнобедренный"),
    (10, 11, 12, "разносторонний"),
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
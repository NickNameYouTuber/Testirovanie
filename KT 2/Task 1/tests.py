import pytest
from main import read_grades_from_csv, calculate_average_grade

@pytest.fixture
def grades_data():
    return read_grades_from_csv('grades.csv')

def test_calculate_average_grade(grades_data):
    actual = calculate_average_grade(grades_data)
    expected = [78.25, 48.0, 44.0, 47.0, 45.0, 46.0, 43.0, 50.0, 83.0, 97.0, 40.0, 45.0, 77.0, 90.0, 4.0, 40.0, 10]

    print(f'Actual: {len(actual)} | Expected: {len(expected)}')
    for i in range(len(actual)):
        if actual[i] != expected[i]:
            print(f'Wrong value: actual {actual[i]} | expected {expected[i]}')
        else:
            print(f'Correct: {actual[i]}')

    assert actual == expected
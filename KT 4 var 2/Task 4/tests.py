import pytest
from main import read_grades_from_csv, calculate_average_grade

def calculate_final_grade(test_scores):
    return sum(test_scores) / len(test_scores)

# Тест с параметризацией
@pytest.mark.parametrize("name, test_scores, expected_final_grade", read_grades_from_csv("grades.csv"))
def test_student_final_grade(name, test_scores, expected_final_grade):
    calculated_final_grade = calculate_final_grade(test_scores)
    assert calculated_final_grade == expected_final_grade
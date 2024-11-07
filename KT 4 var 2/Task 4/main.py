import csv


def read_grades_from_csv(file_path):
    """
    Читает данные из CSV файла и возвращает список словарей с оценками.
    """
    with open("grades.csv", "r") as file:
        csvreader = csv.reader(file)
        grades = [row for row in csvreader]
    return grades


def calculate_average_grade(grades):
    """
    Вычисляет среднее арифметическое для каждого студента.
    """
    averages_list = []
    for grade in grades:
        if grade == grades[0]:
            continue

        print(grade[3], grade[4], grade[5], grade[6])
        average = (float(grade[3]) + float(grade[4]) + float(grade[5]) + float(grade[6])) / 4
        averages_list.append(average)

    return averages_list

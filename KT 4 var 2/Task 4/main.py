import csv


def load_data_from_csv(file_path):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            # Преобразуем оценки и итоговую оценку в числа
            test_scores = [float(row['test1']), float(row['test2']), float(row['test3']), float(row['test4'])]
            final_grade = float(row['final_grade'])
            data.append((row['name'], test_scores, final_grade))
        return data


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

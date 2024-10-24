import json

def get_json_from_file(file_path):
    """
    Загружает данные из JSON файла.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json_to_file(data, file_path):
    """
    Сохраняет данные в JSON файл.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f'Data saved to {file_path}')

def add_json_to_file(file_path, new_superheroes):
    """
    Добавляет новых супергероев в JSON файл.
    """
    print(new_superheroes)
    data = get_json_from_file(file_path)
    data['members'].extend(new_superheroes)
    save_json_to_file(data, file_path)

def sort_json(file_path):
    """
    Сортирует супергероев по возрасту в JSON файле.
    """
    data = get_json_from_file(file_path)
    data['members'].sort(key=lambda x: x['age'])
    save_json_to_file(data, file_path)
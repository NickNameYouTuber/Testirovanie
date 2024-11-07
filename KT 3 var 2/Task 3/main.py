import sqlite3
import pytest


# Фикстура для создания и очистки БД
@pytest.fixture(scope='module', autouse=True)
def db_connection():
    conn = sqlite3.connect(':memory:')  # Создаем базу данных в памяти
    cursor = conn.cursor()

    # Создаем таблицу для тестов
    cursor.execute('''
        CREATE TABLE test_table (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    yield conn  # Возвращаем соединение с базой данных

    # Очистка после теста
    cursor.execute('DROP TABLE test_table')
    conn.close()


# Тесты
def test_insert_into_db(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO test_table (name) VALUES ('test_name')")
    db_connection.commit()

    cursor.execute("SELECT name FROM test_table WHERE id = 1")
    result = cursor.fetchone()

    assert result[0] == 'test_name'


def test_empty_db(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM test_table")
    result = cursor.fetchone()

    assert result[0] == 0
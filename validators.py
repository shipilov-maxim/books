from datetime import datetime, date
from typing import List


def validate_id(new_id: int, existing_ids: set) -> tuple:
    """
    Проверяет уникальность идентификатора. Если не уникальный,
    увеличиваем id.
    """
    while new_id in existing_ids:
        new_id += 1
    existing_ids.add(new_id)
    return new_id, existing_ids


def validate_year(year: str) -> int:
    """
        Проверяет формат года издания.
    """
    try:
        return datetime.strptime(str(year), "%Y").date().year
    except ValueError:
        raise ValueError("Неверный формат даты. Используйте YYYY.")


def validate_status(status: str) -> str:
    """
    Проверяет статус на допустимые варианты.
    """
    valid_status = ['В наличии', 'Выдана']
    if status not in valid_status:
        raise ValueError(f"Статус должен быть одним из: {', '.join(valid_status)}")
    return status


def get_valid_input(prompt: str, valid_choices: List[str] = None) -> str:
    """
    Функция для корректного ввода команды или строкового значения
    """
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == '':
            print("Пожалуйста, введите значение")
        elif valid_choices and user_input not in valid_choices:
            print(f"Пожалуйста, выберите один вариант из: {', '.join(valid_choices)}")
        else:
            return user_input


def get_valid_input_id(prompt: str) -> int:
    """
    Функция для ввода корректного Id
    """
    while True:
        try:
            book_id = int(input(prompt))
            if book_id == '':
                print("Пожалуйста, введите значение")
            else:
                return book_id
        except ValueError:
            print("Пожалуйста, введите корректный номер книги.")


def get_valid_input_year() -> str:
    """
        Функция для ввода корректного года издания
    """
    while True:
        year = input("Введите год издания (YYYY): ")
        try:
            if validate_year(year) < date.today().year:
                return year
            else:
                print("Год издания не должен быть в будущем времени")
        except ValueError as e:
            print(e)

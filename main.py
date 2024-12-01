import json
import os
from json import JSONDecodeError
from typing import Any, List, Dict, Union

from settings import FILE_PATH
from book_manager import BookManager
from validators import get_valid_input, get_valid_input_year, get_valid_input_id


def load_data(file_path: str) -> Any:
    """
    Функция загрузки данных из JSON-файла, обрабатывает исключения, связанные с повреждением данных
    """
    if os.path.exists(file_path):
        if os.path.getsize(file_path) == 0:
            return []
        else:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except JSONDecodeError as e:
                print(f"Некорректные данные в файле. {e}\nПроверьте data.json")
                exit()


def save_data(file_path: str, data: List[Dict[str, Union[int, str]]]) -> None:
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    books = load_data(FILE_PATH)
    book_manager = BookManager(books)

    while True:
        command = get_valid_input("Введите команду (add/view/status/delete/search/exit): ",
                                  valid_choices=['add', 'view', 'status', 'delete', 'search', 'exit'])

        if command == 'add':
            title = get_valid_input("Введите название книги: ")
            author = get_valid_input("Введите автора книги: ")
            year = get_valid_input_year()
            book_manager.add_book(title, author, year)

        elif command == 'view':
            book_manager.view_book()

        elif command == 'status':
            task_id = get_valid_input_id("Введите ID книги для смены статуса: ")
            book_manager.status_book(task_id)

        elif command == 'delete':
            try:
                task_id = int(input("Введите ID книги для удаления: "))
                book_manager.delete_book(task_id)
            except ValueError:
                print("Пожалуйста, введите корректный номер книги.")

        elif command == 'search':
            keyword = input("Введите ключевое слово для поиска: ")
            book_manager.search_book(keyword)

        elif command == 'exit':
            save_data(FILE_PATH, book_manager.get_all_books())
            break


if __name__ == "__main__":
    main()

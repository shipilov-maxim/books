from typing import Dict, Union

from validators import validate_year, validate_status, validate_id


class Book:
    existing_ids = set()

    def __init__(self, book_id: int, title: str, author: str, year: str, status="В наличии") -> None:
        """
        В момент инициализации проходят проверки по полям
        """
        self.id, self.existing_ids = validate_id(book_id, self.existing_ids)
        self.title: str = title.title()
        self.author: str = author.title()
        self.year: int = validate_year(year)
        self.status: str = validate_status(status)

    def __str__(self) -> str:
        """
        Строковое представление объекта
        """
        return f"""
            Id: {self.id},
            Название: {self.title},
            Автор: {self.author},
            Год издания: {self.year},
            Статус: {self.status}
        """

    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Метод, который возвращает словарь
        ключ - название атрибута: значение - значение атрибута
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

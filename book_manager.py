from typing import List, Dict, Union

from book import Book


class BookManager:

    def __init__(self, books: List[Dict]) -> None:
        """
        Инициализирует существующие книги и выводит информацию об исключениях и ошибках, если такие будут
        """
        books_list = []
        for book in books:
            try:
                books_list.append(
                    Book(
                        book_id=book['id'],
                        title=book['title'],
                        author=book['author'],
                        year=book['year'],
                        status=book['status']
                    )
                )
            except ValueError as e:
                print(f"Некорректные данные в книге №{book['id']}: {e}\nПроверьте data.json")
                exit()
        self.books: List[Book] = books_list

    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Добавляет к списку экземпляров книг новый объект
        """
        book_id = len(self.books) + 1
        book = Book(book_id, title, author, year)
        self.books.append(book)
        print(f"Книга добавлена: {title.title()}")

    def view_book(self) -> List[Book]:
        """
        Выводит в консоль информацию о всех книгах и возвращает список экземпляров
        """
        books = [book for book in self.books]
        if len(books) == 0:
            print("Книг нет")
        else:
            for book in books:
                print(book)
            return books

    def status_book(self, book_id: int) -> None:
        """
        Меняет статус книги на противоположный
        """
        for book in self.books:
            if book.id == book_id:
                if book.status == "Выдана":
                    book.status = "В наличии"
                    print(f"Книга {book_id} отмечена как в наличии.")
                elif book.status == "В наличии":
                    book.status = "Выдана"
                    print(f"Книга {book_id} отмечена как выданная.")
                return
            else:
                print("Книга не найдена.")

    def delete_book(self, book_id: int) -> None:
        """
        Пересобирает список без книги с указанным ID. Если такой книги не будет,
        список не изменится и выведется сообщение о том, что книга не найдена.
        """
        initial_count = len(self.books)
        self.books = [book for book in self.books if book.id != book_id]
        if len(self.books) < initial_count:
            print(f"Книга {book_id} удалена.")
        else:
            print("Книга не найдена.")

    def search_book(self, key: str) -> List[Book]:
        """
        Выводит информацию в консоль и возвращает список экземпляров обо всех книгах,
        у которых есть совпадение ключевого слова с названием, автором или годом издания.
        """
        found_books = [book for book in self.books if key.lower() in book.title.lower() or
                       key.lower() in book.author.lower() or key.lower() in str(book.year)]
        for book in found_books:
            print(book)
        return found_books

    def get_all_books(self) -> List[Dict[str, Union[int, str]]]:
        """
        Возвращает список словарей перед закрытием приложения для сохранения в JSON-файл
        """
        return [book.to_dict() for book in self.books]

import pytest

from book import Book
from book_manager import BookManager


@pytest.fixture()
def setup_book_manager():
    books = [
        {
            "id": 1,
            "title": "Test Book 1",
            "author": "author 1",
            "year": "2023",
            "status": "В наличии"
        },
        {
            "id": 2,
            "title": "Test Book 2",
            "author": "author 2",
            "year": "2023",
            "status": "В наличии"
        },
    ]
    return BookManager(books)


@pytest.fixture()
def reset_book_ids():
    Book.existing_ids = set()


def test_add_book(reset_book_ids, setup_book_manager):
    setup_book_manager.add_book("Test Book 3", "author 3", "2023")
    assert len(setup_book_manager.books) == 3
    assert setup_book_manager.books[2].title == "Test Book 3"


def test_view_book(reset_book_ids, setup_book_manager):
    setup_book_manager.view_book()
    assert len(setup_book_manager.books) == 2


def test_status_book(reset_book_ids, setup_book_manager):
    setup_book_manager.status_book(1)
    assert setup_book_manager.books[0].status == "Выдана"
    setup_book_manager.status_book(1)
    assert setup_book_manager.books[0].status == "В наличии"


def test_delete_book(reset_book_ids, setup_book_manager):
    setup_book_manager.delete_book(1)
    assert len(setup_book_manager.books) == 1


def test_search_book(reset_book_ids, setup_book_manager):
    assert setup_book_manager.search_book("Book 2")[0].title == "Test Book 2"

import unittest
from librairie.book import Book
from librairie.library import Library

@pytest.fixture
def library():
    return Library()

@pytest.fixture
def book():
    return Book("Test Book", "Author Name")

def test_add_book(library, book):
    library.add_book(book)
    assert book in library.books

def test_remove_book(library, book):
    library.add_book(book)
    library.remove_book(book)
    assert book not in library.books

def test_remove_book_not_in_library(library, book):
    with pytest.raises(ValueError):
        library.remove_book(book)

def test_find_book_by_title(library, book):
    library.add_book(book)
    found_book = library.find_book_by_title("Test Book")
    assert found_book == book

def test_find_book_by_title_not_found(library):
    found_book = library.find_book_by_title("Nonexistent Book")
    assert found_book is None

def test_list_books(library, book):
    library.add_book(book)
    books_list = library.list_books()
    assert books_list == [str(book)]

def test_list_books_empty(library):
    books_list = library.list_books()
    assert books_list == []

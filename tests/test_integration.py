import pytest

from librairie.book import Book
from librairie.library import Library

def test_add_and_list_books():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    
    library.add_book(book1)
    library.add_book(book2)
    
    assert len(library.list_books()) == 2
    assert str(book1) in library.list_books()
    assert str(book2) in library.list_books()

def test_remove_book():
    library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    
    library.add_book(book1)
    library.add_book(book2)
    
    library.remove_book(book1)
    

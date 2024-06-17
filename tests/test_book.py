import pytest
from librairie.book import Book 
# Assurez-vous que le fichier contenant 
# la classe Book s'appelle book.py

def test_book_initialization():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    assert book.title == "The Great Gatsby"
    assert book.author == "F. Scott Fitzgerald"

def test_book_str():
    book = Book("1984", "George Orwell")
    assert str(book) == "1984 by George Orwell"

if __name__ == "__main__":
    pytest.main()

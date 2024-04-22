from many_to_many import Author, Book, Contract
import pytest

def test_book_init():
    """Test Book class initializes with title"""
    book = Book("Title")
    assert book.title == "Title"

def test_author_init():
    """Test Author class initializes with name"""
    author = Author("Name")
    assert author.name == "Name"

class TestContract:
    all_contracts = []

    def test_contract_init(self):
        """Test Contract class initializes with author, book, date, royalties"""
        book = Book("Title")
        author = Author("Name")
        date = '01/01/2001'
        royalties = 40000
        contract = Contract(author, book, date, royalties)

        assert contract.author == author
        assert contract.book == book
        assert contract.date == date
        assert contract.royalties == royalties

    def test_contract_validates_author(self):
        """Test Contract class validates author of type Author"""
        book = Book("Title")
        date = '01/01/2001'
        royalties = 40000

        with pytest.raises(Exception):
            Contract("Author", book, date, royalties)

    def test_contract_validates_book(self):
        """Test Contract class validates book of type Book"""
        author = Author("Name")
        date = '01/01/2001'
        royalties = 40000

        with pytest.raises(Exception):
            Contract(author, "Book", date, royalties)

    def test_contract_validates_date(self):
        """Test Contract class validates date of type str"""
        author = Author("Name")
        book = Book("Title")
        royalties = 40000
        # Pass an integer as the date to intentionally trigger an exception
        with pytest.raises(Exception):
            Contract(author, book, 1012001, royalties)

    def test_contract_validates_royalties(self):
        """Test Contract class validates royalties of type int"""
        author = Author("Name")
        book = Book("Title")
        date = '01/01/2001'

        with pytest.raises(Exception):
            Contract(author, book, date, "Royalties")

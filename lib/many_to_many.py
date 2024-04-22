class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.all_contracts = []
        self.all_authors.append(self)

    def contracts(self):
        return self.all_contracts

    def books(self):
        return [contract.book for contract in self.all_contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of Book")
        contract = Contract(self, book, date, royalties)
        self.all_contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.all_contracts)


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("The date must be a string")
        if not isinstance(royalties, int):
            raise Exception("The royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

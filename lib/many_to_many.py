class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Return a list of contracts with the specified attribute and value
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Return a list of books with the specified attribute and value
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # this will return new Contract object
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # returns a list of its authors
        return [contract for contract in Contract.all if contract.book == self]

    # author() => returns a list of its authors
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author  # should be an instance of Author class
        self.book = book  # should be an instance of Book class
        self.date = date  # string
        self.royalties = royalties  # integer(number of royalties)
        Contract.all.append(self)

    # Contract validates author of type Author, and book
    @property
    def author(self):  # getter for type Author
        return self._author

    @author.setter
    # setter will validate author of type Author
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError("Author must be an instance of Author")

    @property
    def book(self):  # getter for type Book
        return self._book

    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise ValueError("Book must be an instance of Book")

    # manage the type of date => should be string

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise ValueError("Date must be a string")

    @property
    # check royalties type int
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise ValueError("Royalties must be an integer")

    @classmethod
    def contracts_by_date(cls, date):
        # this should return all contracts that have the same date as the date passed into method.
        return [contract for contract in cls.all if contract.date == date]


# all setters should raise an exception  upon failure
# all classes should also keep track of all members using a class variable
# Contract is an intermediary between author and specified book w date and royalties

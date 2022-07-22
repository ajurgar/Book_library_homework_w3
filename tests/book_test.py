import unittest
from models.book import Book


class TestBook(unittest.TestCase):

    def setUp(self):

        self.book1 = Book("The Constitution of Liberty", "F. Hayek", "Economy")
        self.book2 = Book("Zero to One", "Peter Thiel", "Business")
        self.book3 = Book("Rich Dad, Poor Dad", "Robert Kiyosaki", "Finance")


        books = [self.book1, self.book2, self.book3]

    def test_book_has_title(self):
        self.assertEqual("The Constitution of Liberty", self.book1.title)

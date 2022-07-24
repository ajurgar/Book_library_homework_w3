import unittest
from models.book import Book
import datetime


class TestBook(unittest.TestCase):

    def setUp(self):

        self.book1 = Book("The Constitution of Liberty", "F. Hayek", "Economy", False, datetime.date(2022, 6, 17))
        self.book2 = Book("Zero to One", "Peter Thiel", "Business", True, datetime.date(2022, 4, 7))
        self.book3 = Book("Rich Dad, Poor Dad", "Robert Kiyosaki", "Finance", True, datetime.date(2022, 5, 23))


        books = [self.book1, self.book2, self.book3]

    def test_book_has_title(self):
        self.assertEqual("The Constitution of Liberty", self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("Peter Thiel", self.book2.author)

    def test_book_has_genre(self):
        self.assertEqual("Finance", self.book3.genre)

    def test_book_has_checked_out(self):
        self.assertEqual(False, self.book1.checked_out)

    


    

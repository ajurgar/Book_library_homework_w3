from models.book import Book


book1 = Book("The Constitution of Liberty", "F. Hayek", "Economy")
book2 = Book("Zero to One", "Peter Thiel", "Business")
book3 = Book("Rich Dad, Poor Dad", "Robert Kiyosaki", "Finance")


books = [book1, book2, book3]


def add_book(new_book):
    books.append(new_book)


def delete_book(book_title):
        
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break
        books.remove(book_title)


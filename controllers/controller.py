from flask import render_template, request, redirect
from app import app
from models.book import *
from models.list_book import *


@app.route("/books", methods=['GET'])
def index():
    return render_template("books/index.html", title="Book Library", books=books)


@app.route("/books/<index>")
def book(index):
    book = books[int(index)]
    return render_template("books/view.html", title="Book View", book=book, book_index=index)


@app.route("/books/new")
def new():
    return render_template("books/new.html", title="New Book")


@app.route("/books", methods=["POST"])
def add():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    checked_out = request.form["checked-out"]
    return_by = request.form["return-by"]
    new_book = Book(title, author, genre, checked_out, return_by)
    add_book(new_book)
    return redirect("/books")


@app.route("/books/delete", methods=["POST"])
def delete():
    delete_book(request.form["title"])
    return redirect("/books")

@app.route("/books/<index>", methods=["POST"])
def check(index):
    book = books[int(index)]

    user_selection = request.form["checked-out"] #This comes as a string

    if user_selection == "check-in":
        check_in(book)
    if user_selection == "check-out":
        check_out(book)
   
    return redirect("/books")
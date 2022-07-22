from flask import render_template, request, redirect
from app import app
from models.book import *
from models.list_book import *


@app.route("/books")
def index():
    return render_template("books/index.html", title="Book Library", books=books)


@app.route("/books/<index>")
def book(index):
    book = books[int(index)]
    return render_template("books/view.html", title="Book View", book=book)


@app.route("/books/new")
def new():
    return render_template("books/new.html", title="New Book")


@app.route("/books", methods=["POST"])
def add():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_book(new_book)
    return redirect("/books")


@app.route("/books/delete/<name>", methods=["POST"])
def delete(name):
    delete_book(name)
    return redirect("/books")

import mysql.connector
import re

class DatabaseManager:
    def __init__(self):
        self.connector = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Dieng",
            database = "POO_Books",
            auth_plugin='mysql_native_password'
            )
        self.cursor = self.connector.cursor()

    def commit(self):
        self.connector.commit()
        self.cursor.close()

class Book:
    def __init__(self, title, author, avalaibility = True ):
        self.title = title
        self.author = author
        self.avalaibility = avalaibility



class BookManager():
    db= DatabaseManager()
    def add_book(self, book):
            try:
                while True:
                    title = input("Title : ").capitalize()
                    if re.match(r'[a-zA-Z0-9]+$', title):
                        break
                    else:
                        raise ValueError("Title must be written by letters and numbers")
                
                while True:
                    author = input("Author : ").capitalize()
                    if re.match(r'[a-zA]')
                    break

                query = """INSERT INTO Books (title, author) values (%s, %s )"""
                self.db.cursor.execute(query, (book.title, book.author))
                self.db.commit()
                print()
                return True
            except Exception as e :
                print()


class Menu:
    book_manager = BookManager()


    def start(self):
        print("===MENU=== \n" \
        "1. Add a book \n")


        choice = input("Choice : ").strip()
        match choice :
            case "1":
                title = input("Title : ").capitalize()
                author = input("Author : ").capitalize()

                book = Book(title, author)
                print(self.book_manager.add_book(book))


menu = Menu()
menu.start()
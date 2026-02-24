import mysql.connector

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
    def __init__(self,id_book, title, author, avalaibility = True ):
        self.id_book = id_book
        self.title = title
        self.author = author
        self.avalaibility = avalaibility



class BookManager():
    db= DatabaseManager()
    def add_book(self, title, author):
        query = """INSERT INTO Books (title, author) values (%s, %s )"""
        self.db.cursor.execute(query, (title,author))
        self.db.commit()
        return self.db.cursor.lastrowid
    

bookmanager = BookManager()
bookmanager.add_book("Os de Mor LAM", "Birago DIOP")
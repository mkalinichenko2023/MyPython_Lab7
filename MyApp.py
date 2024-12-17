from flask import Flask, render_template
import sqlite3
MyApp = Flask(__name__)

@MyApp.route('/')
def index():
    conn = sqlite3.connect('my_book_list.db')
    conn.row_factory = sqlite3.Row
    books = conn.execute('select * from MyBookList order by BookStatus ').fetchall()
    conn.close()
    return render_template('booklst.html', books=books)

if __name__ == '__main__':
    MyApp.run()

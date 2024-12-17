import sqlite3

def main():
    #соединение с БД
    conn= sqlite3.connect('my_book_list.db')
    #получить курсор
    cur= conn.cursor()

    #создать таблицу с данными теста, если ее нет
    cur.execute('''create table if not exists MyBookList(IdBook     integer primary key AUTOINCREMENT,
                                                         BookName   text,
                                                         Author     text,
                                                         PagesCnt   integer,
                                                         BookStatus text,
                                                         BookBall   integer)''')
    conn.commit()

    #подготовка  к вводу вопросов теста
    Answer= 'да'
    AuthNm= ' '
    BookNm= ' '
    BookSt= ' '
    PagesC= 0
    BookBl= 0

    #цикл ввода
    while Answer == 'да':
        BookNm= input('Название книги: ')
        AuthNm= input('Автор книги: ')
        BookSt= input('Статус (прочитана / в ожидании прочтения): ')
        PagesC= int(input('Кол-во страниц: '))
        BookBl= int(input('Оценка читателя от 1 до 10 (для неппрочитанных - 0):'))

        #сохранить в таблицу
        cur.execute('''insert into MyBookList(BookName, Author, PagesCnt, BookStatus, BookBall)
                                   values(?, ?, ?, ?, ?)''',
                                   (BookNm, AuthNm, PagesC, BookSt, BookBl))
        conn.commit()

        Answer= input('Вы хотите продолжить ввод книг? (да/нет):')
        Answer= Answer.lower()


    #посмотрим список книг черз Python
    cur.execute('select IdBook, BookName, Author, PagesCnt, BookStatus, BookBall from MyBookList order by IdBook')
    results= cur.fetchall()
    print()
    print('Список книг к прочтению:')
    print('Номер Название                           Автор               Кол-во стр Статус         Оценка')
    for Rec in results:
        print(f'{Rec[0]:^5} {Rec[1]:35} {Rec[2]:20} {Rec[3]:10} {Rec[4]:15} {Rec[5]}')

    #закрыть соединение
    conn.close()

#главная функция
if __name__ == '__main__':
    main()

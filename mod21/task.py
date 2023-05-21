import csv

from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String, Date, DateTime, Float, Boolean, \
    ForeignKey, func
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref
from datetime import datetime, timedelta, date
from flask import Flask, jsonify, request

app = Flask(__name__)
engine = create_engine("sqlite:///mod21.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default="1")
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', backref=backref('books', cascade='all, ' 'delete-orphan', lazy='select'))
    students = relationship('Receiving_book', back_populates='book')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)
    books = relationship('Receiving_book', back_populates='student')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Receiving_book(Base):
    __tablename__ = 'receiving_books'

    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    date_of_issue = Column(DateTime, default=datetime.now)
    date_of_return = Column(DateTime, nullable=True)

    student = relationship('Student', back_populates='books')
    book = relationship('Book', back_populates='students')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

"""def insert_data():
    authors = [Author(name="Александр", surname="Пушкин"),
                Author(name="Лев", surname="Толстой"),
                Author(name="Михаил", surname="Булгаков"),]
    authors[0].books.extend([Book(name="Капитанская дочка",
                                count=5,
                                release_date=date(1836, 1, 1)),
                            Book(name="Евгений Онегин",
                                count=3,
                                release_date=date(1838, 1, 1))
                                ])
    authors[1].books.extend([Book(name="Война и мир",
                                count=10,
                                release_date=date(1867, 1, 1)),
                            Book(name="Анна Каренина",
                                count=7,
                                release_date=date(1877, 1, 1))
                                ])
    authors[2].books.extend([Book(name="Морфий",
                                count=5,
                                release_date=date(1926, 1, 1)),
                            Book(name="Собачье сердце",
                                count=3,
                                release_date=date(1925, 1, 1))
                                ])

    students = [Student(name="Nik", surname="1", phone="2", email="3",
                        average_score=4.5,
                        scholarship=True),
                Student(name="Vlad", surname="1", phone="2", email="3",
                        average_score=4,
                        scholarship=True),
                ]

    session.add_all(authors)
    session.add_all(students)
    session.commit()

def give_me_book():
    nikita = session.query(Student).filter(Student.name == 'Nik').one()
    vlad = session.query(Student).filter(Student.name == 'Vlad').one()
    books_to_nik = session.query(Book).filter(Author.surname == 'Толстой', Author.id == Book.author_id).all()
    books_to_vlad = session.query(Book).filter(Book.id.in_([1, 3, 4])).all()
    for book in books_to_nik:
        receiving_book = Receiving_book()
        receiving_book.book = book
        receiving_book.student = nikita
        session. add(receiving_book)
    for book in books_to_vlad:
        receiving_book = Receiving_book()
        receiving_book.book = book
        receiving_book.student = vlad
        session. add(receiving_book)

    session.commit()"""

@app.before_request
def before_request_func():
    Base.metadata.create_all(bind=engine)


@app.route('/')
def hello():
    return "Hello World"

@app.route('/books_by_author/<int:author_id>')
def books_by_author(author_id):
    available_books = session.query(Book).filter(Book.author_id == author_id, Book.id == Receiving_book.book_id, Receiving_book.date_of_return == None).all()
    books_list = []
    for book in available_books:
        json_book = book.to_json()
        books_list.append(json_book)
    return jsonify(available_books_list=books_list), 200


@app.route('/books_by_student/<int:student_id>')
def books_by_student(student_id):
    books_id = session.query(Receiving_book.book_id).distinct().filter(Receiving_book.book_id == Book.id, Receiving_book.student_id == student_id).all()
    books_id = [item[0] for item in books_id]
    authors_id = session.query(Book.author_id).distinct().filter(Receiving_book.book_id == Book.id, Receiving_book.student_id == student_id).all()
    authors_id = [item[0] for item in authors_id]
    books_by_authors = session.query(Book).distinct().filter(Book.author_id.in_(authors_id), Book.id.notin_(books_id)).all()
    books_list = []
    for book in books_by_authors:
        json_book = book.to_json()
        books_list.append(json_book)
    return jsonify(recomended_books_list=books_list), 200

@app.route('/books/month', methods=['GET'])
def book_of_the_month():
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_month_start = datetime(current_year, current_month, 1, 0, 0, 0, 0)
    taken_books_count = session.query(func.count(Receiving_book.book_id)).filter(Receiving_book.date_of_issue >= current_month_start).scalar()
    students_count = session.query(func.count(Student.id)).scalar()
    avg_book_month_count = round(taken_books_count / students_count, 3)
    return f'Среднее количество книг в этом месяце {avg_book_month_count}', 200

@app.route('/books/popular', methods=['GET'])
def the_most_popular_book():
    book_id = session.query(func.count(Receiving_book.book_id)). \
        filter(Receiving_book.student_id == Student.id, Student.average_score >= 4.0).group_by(Receiving_book.book_id). \
        order_by(func.count(Receiving_book.book_id).desc()).limit(1).all()
    book = session.query(Book).filter(Book.id == book_id[0][0]).all()
    json_book = book[0].to_json()
    return jsonify(the_most_popular_book=json_book), 200

@app.route('/students', methods=['GET', "POST"])
def students():
    if request.method == 'GET':
        current_year = datetime.now().year
        current_year_start = datetime(current_year, 1, 1, 0, 0, 0, 0)
        students = session.query(Student). \
            filter(Receiving_book.student_id == Student.id, Receiving_book.date_of_issue >= current_year_start). \
            group_by(Receiving_book.student_id).order_by(func.count(Receiving_book.student_id).desc()).limit(10).all()
        students_list = []
        for student in students:
            json_student = student.to_json()
            students_list.append(json_student)
        return jsonify(top_10_readers_of_the_year=students_list), 200

    elif request.method == 'POST':
        stud_file = request.files.get('students_file')
        if stud_file:
            try:
                stud_file.save('students.csv')
                stud_list = []
                with open('students.csv', 'r', newline='') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for student in reader:
                        if student['scholarship'].lower() == 'true':
                            student['scholarship'] = True
                        elif student['scholarship'].lower() == 'false':
                            student['scholarship'] = False
                        stud_list.append(student)
                session.bulk_insert_mappings(Student, stud_list)
            except Exception as e:
                print(e)
                return 'Ошибка при обработке файла "students"', 400
            session.commit()
            return 'Студенты из файла "students" были добавлены', 200
        return 'Файл "students_file" не найден', 400

if __name__ == "__main__":
    app.run()
    """Base.metadata.create_all(bind=engine)
    check_exist = session.query(Author).all()
    if not check_exist:
        insert_data()
        give_me_book()"""

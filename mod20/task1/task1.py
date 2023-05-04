from sqlalchemy import create_engine, Column, Integer, String, DATE, MetaData, FLOAT, BOOLEAN, DATETIME
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.exc import NoResultFound
from flask import Flask, jsonify, abort, request
from datetime import datetime, timedelta

app = Flask(__name__)
engine = create_engine('sqlite:///python.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(DATE, nullable=False)
    author_id = Column(Integer, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Authors(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(FLOAT, nullable=False)
    scholarship = Column(BOOLEAN, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_all_scholarship_students(cls):
        return session.query(Students).filter(Students.scholarship == True).all()

    @classmethod
    def get_all_good_students(cls, score: float):
        return session.query(Students).filter(Students.average_score > score).all()


class Receiving_books(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DATETIME, nullable=False)
    date_of_return = Column(DATETIME)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @hybrid_property
    def count_date_with_book(self):
        try:
            return self.date_of_return - self.date_of_issue
        except:
            return "Книгу еще не сдали"

@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/get_books')
def get_books():
    books = session.query(Books).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200

@app.route('/get_books_by_name/<string:name>')
def get_books_by_name(name):
    books = session.query(Books).filter(Books.name.like(f"%{name}%")).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200

@app.route('/get_robber')
def get_robber():
    books = session.query(Receiving_books).filter(Receiving_books.date_of_issue < datetime.now() - timedelta(days=14)).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200

@app.route('/issue_book', methods = ['POST'])
def issue_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    date_of_issue = request.form.get('date_of_issue', type=str)
    new_issue = Receiving_books(book_id=book_id,
                                student_id=student_id,
                                date_of_issue=datetime.strptime(date_of_issue, '%Y-%m-%d %H:%M:%S:%f'))
    session.add(new_issue)
    session.commit()
    return "Книга выдана", 201

@app.route('/pass_book', methods = ['POST'])
def pass_book():
    try:
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        book = session.query(Receiving_books).filter(Receiving_books.book_id == book_id).filter((Receiving_books.student_id == student_id)).one()
        book.date_of_return = datetime.now()
        session.commit()
        return "Книга сдана"
    except NoResultFound:
        return 'Такой связки id не существует'

if __name__ == "__main__":
    app.run()
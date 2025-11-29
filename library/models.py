from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

# 1. Author modeli
class Author(Base):
    __tablename__ = "authors"

    author_id = Column('id',Integer, primary_key=True)
    name = Column('name',String(100), nullable=False)
    bio = Column('bio',Text, nullable=True)
    created_at = Column('created_at',DateTime, default=datetime.now)

    books = relationship("Book", back_populates="author")


# 2. Book modeli
class Book(Base):
    __tablename__ = "books"

    book_id = Column('id',Integer, primary_key=True)
    title = Column('title',String(200), nullable=False)
    author_id = Column('author_id',Integer, ForeignKey("authors.id",ondelete="SET NULL"))
    published_year = Column('published_year',Integer)
    isbn = Column('isbn',String(13), unique=True, nullable=True) # bo'sh bolishi mumkin emas
    is_available = Column('is_available',Boolean, default=True)
    created_at = Column('created_at',DateTime, default=datetime.now)
    updated_at = Column('updated_at',DateTime, default=datetime.now)

    author = relationship("Author", back_populates="books")
    borrows = relationship("Borrow", back_populates="book")


# 3. Student moduli
class Student(Base):
    __tablename__ = "students"

    student_id = Column('id',Integer, primary_key=True)
    full_name = Column('full_name',String(150), nullable=False)
    email = Column('email',String(100), unique=True, nullable=False)
    grade = Column('grade',String(20), nullable=True)
    registered_at = Column('registered_at',DateTime, default=datetime.now)

    borrows = relationship("Borrow", back_populates="student")


# 4. Borrow moduli
class Borrow(Base):
    __tablename__ = "borrows"

    borrow_id = Column('id',Integer, primary_key=True)
    student_id = Column('student_id',Integer, ForeignKey("students.id",ondelete='CASCADE'))
    book_id = Column('book_id',Integer, ForeignKey("books.id",ondelete='CASCADE'))
    borrowed_at = Column('borrowed_at',DateTime, default=datetime.now)
    due_date = Column('due_date',DateTime, default=lambda: datetime.now)
    returned_at = Column('returned_at',DateTime, nullable=True)

    student = relationship("Student", back_populates="borrows")
    book = relationship("Book", back_populates="borrows")

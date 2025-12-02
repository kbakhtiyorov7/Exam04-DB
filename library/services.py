from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from .models import Author,Book,Student,Borrow
from .db import get_db

# =========== AUTHOR CRUD ==========

def create_author(name: str, bio: str = None) -> Author:
    """Yangi muallif yaratish"""
    with get_db() as session: #session yaratish
        author = Author(
            name = name,
            bio = bio
        )
        session.add(author)  #authorni qo'shadi
        session.commit()     # uni databasega saqlaydi
        return author

def get_author_by_id(author_id: int) -> Author | None:
    """ID bo'yicha muallifni olish"""

    with get_db() as session:
       author = session.query(Author).filter(Author.author_id == author_id).first()
       return author
    

def get_all_authors() -> list[Author]:
    """Barcha mualliflar ro'yxatini olish"""
    with get_db() as session:
        authors = session.query(Author).all()
        return authors

def update_author(author_id: int, name: str = None, bio: str = None) -> Author | None:
    """Muallif ma'lumotlarini yangilash"""
    with get_db() as session:
        author = session.query(Author).filter(Author.author_id == author_id).first()
        if author is None:
            return None
        if name is not None:
            author.name = name
        if bio is not None:
            author.bio = bio

        session.commit()
        return author

# update author: avvalo berilgan id da author bor yoki yo'qligi tekshiriladi
#Agar bor bo'lsa uning name hamda bio qismlari yangi bio va namega o'zgartiriladi

def delete_author(author_id: int) -> bool:
    """Muallifni o'chirish (faqat kitoblari bo'lmagan holda)"""
    with get_db() as session:
        author = session.query(Author).filter(Author.author_id == author_id).first()
        if author is None:
            return False

        session.delete(author)
        session.commit()
        return True

# delete:
# Agar author bor bo'lsa u o'chriladi lekin kitobi esa o'chmaydi


# =============== BOOK CRUD ===================

def create_book(title: str, author_id: int, published_year: int, isbn: str = None) -> Book:
    """Yangi kitob yaratish"""
    with get_db() as session:
        book = Book(
            title = title,
            author_id = author_id,
            published_year = published_year,
            isbn = isbn
        )
        session.add(book)
        session.commit()
        return book

def get_book_by_id(book_id: int) -> Book | None:
    """ID bo'yicha kitobni olish"""
    with get_db() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        return book
    

def get_all_books() -> list[Book]:
    """Barcha kitoblar ro'yxatini olish"""
    with get_db() as session:
        books = session.query(Book.title).all()

        return books

def search_books_by_title(title: str) -> list[Book]:
    """Kitoblarni sarlavha bo'yicha qidirish (partial match)"""
    with get_db() as session:
        books = session.query(Book).filter(
            Book.title.ilike(f"%{title}%")
        ).all()
        return books

def delete_book(book_id: int) -> bool:
    """Kitobni o'chirish"""
    with get_db() as session:
        delete_book = session.query(Book).filter(Book.book_id == book_id).first()
        if delete_book is None:
            return False

        session.delete(delete_book)
        session.commit()
        return True
    
    
# ==============   Student Crud ===================

def create_student(full_name: str, email: str, grade: str = None) -> Student:
    """Yangi talaba ro'yxatdan o'tkazish"""
    with get_db() as session:
        student = Student(
            full_name = full_name,
            email = email,
            grade = grade
        )
        session.add(student)
        session.commit()
        return student


def get_student_by_id(student_id: int) -> Student | None:
    """ID bo'yicha talabani olish"""
    with get_db() as session:
        student = session.query(Student).filter(Student.student_id == student_id).first()
        return student
    


def get_all_students() -> list[Student]:
    """Barcha talabalar ro'yxatini olish"""
    with get_db() as session:
        students = session.query(Student).all()
        return students

def update_student_grade(student_id: int, grade: str) -> Student | None:
    """Talaba sinfini yangilash"""
    with get_db() as session:
        updated_student = session.query(Student).filter(Student.student_id == student_id).first()
        
        if updated_student is None:
            return None
    
        updated_student.grade = grade
        session.commit() 
        return  updated_student




# =============== Qo'shimcha Crudlar =====================

def borrow_book(student_id: int, book_id: int) -> Borrow | None:
    """
    Talabaga kitob berish
    
    Quyidagilarni tekshirish kerak:
    1. Student va Book mavjudligini
    2. Kitobning is_available=True ekanligini
    3. Talabada 3 tadan ortiq qaytarilmagan kitob yo'qligini yani 3 tagacha kitob borrow qila oladi
    
    Transaction ichida:
    - Borrow yozuvi yaratish
    - Book.is_available = False qilish
    - due_date ni hisoblash (14 kun)
    
    Returns:
        Borrow object yoki None (xatolik bo'lsa)
    """
    with get_db() as session:
        student = session.query(Student).filter(Student.student_id == student_id).first()
        book = session.query(Book).filter(Book.book_id == book_id).first()

        if book is None or student is None:     # Book yoki student yo'q bo'lsa Ishlamaydi
            print("Student or Book is None")
            return None
        
        if book.is_available == False:   #Kitobni bor ekanligini tekshiradi agat yuq bo'lsa 
            print("Kitob band")          # None qaytaradi va tugaydi
            return None
        
        # borrow_books = session.query(Borrow).filter(Borrow.student_id == student).all().count()
        # bu yog'i o'xshamay qoldi, yoza olmadim xato yozdim

        borrow = Borrow(
            student_id=student_id,
            book_id=book_id,
            borrowed_at=datetime.now(),
            due_date=datetime.now() + timedelta(days=14) #timedeltani o'rganib keyin qo'shdim
        )
        session.add(borrow)

        book.is_available = False

        session.commit()
        return borrow
    
def return_book(borrow_id: int) -> bool:
    """
    Kitobni qaytarish
    
    Transaction ichida:
    - Borrow.returned_at ni to'ldirish
    - Book.is_available = True qilish
    
    Returns:
        True (muvaffaqiyatli) yoki False (xatolik)
    """
    with get_db() as session:
        borrow = session.query(Borrow).filter(
            Borrow.borrow_id == borrow_id).first()

        if borrow is None:
            print("Borrow topilmadi yoki kitob  qaytarilgan")
            return False

        borrow.returned_at = datetime.now()

        book = session.query(Book).filter(Book.book_id == borrow.book_id).first()
        if book:
            book.is_available = True

        session.commit()
        return True

       




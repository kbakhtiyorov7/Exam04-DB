from datetime import datetime
from sqlalchemy import or_, not_, and_
from sqlalchemy.orm import Session
from .models import Author,Book,Student,Borrow
from .db import get_db


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
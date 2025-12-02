from datetime import date
from library.create_tables import init_db
from library.services import (
    create_author,
    get_author_by_id,
    get_all_authors,
    update_author,
    delete_author,
    create_book,
    get_book_by_id,
    get_all_books,
    search_books_by_title,
    delete_book,
    create_student,
    get_student_by_id,
    get_all_students,
    update_student_grade,
    borrow_book,
    return_book
)
from demo_data import demo_authors,books_demo, students_demo

init_db()

# ======================= AUTHOR CRUD =======================

# create_author('James','Atomic habits kitobini yozgan')  # 1 ta author qo'shildi

# for author in demo_authors:
    # create_author(author[0],author[1])   #40 da demo data qo'shib oldim

# author = get_author_by_id(1)
# print(author.name)             # 1-idga ega authorni olish


# authors = get_all_authors()
# for author in authors:
#     print(author.name)         # hamma authorlarni olish va ularni chiqarish


# updated_author = update_author(55,"James","Atomic habits kitobi muallifi")
# if updated_author is None:
#     print(" Bu id dagi author topilmadi!")
# else:
#     print("Author yangilandi")         # agar berilgan id dagi author topilmasa author topilmadi deb chiqaradi



# if delete_author(1):
#     print("Author o'chirildi")
# else:
#     print("Author topilmadi")


# ============= BOOK CRUD ==============

# create_book("Atomic habits",3,2015,'1002300189758')   # 1 da malumot qo'shildi
# for book  in books_demo:
#     create_book(book[0],book[1],book[2],book[3])  # 40 da data qo'shildi

# book = get_book_by_id(6)
# print(book.title)         # berilgan id dagi kitobning titlesini chiqarish


# books = get_all_books()
# for book in books:
#     print(book)           # kitoblarning title sini chiqarish

# books = search_books_by_title("Book Title 2")
# for book in books:
#     print(book.title)

# deleted_book = delete_book(9)
# if delete_book:
#     print("Kitob o'chirildi")
# else:
#     print("Kitob topilmadi")


# ======================== Student Crud  ============================


# create_student("Ali Valiyev",'Valiyev@gmail.com','2-kurs')
# for student in students_demo:
    # create_student(student[0],student[1],student[2])  # 40 ta student qo'shildi


# print(get_student_by_id(5).full_name)


# students = get_all_students()
# for student in students:
#     print(student.full_name)


# updated_student = update_student_grade(6, "E")
# if updated_student is None:
#     print("Student topilmadi")
# else:
#     print("Student yangilandi:", updated_student.full_name)


# ============== Qo'shimcha Crudlar =======================

# borrow_book = borrow_book(21,21)   # borrow qilish bajarildi
# print(borrow_book)

# ret_book = return_book(1)
# print(ret_book)

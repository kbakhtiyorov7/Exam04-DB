from datetime import date
from library.create_tables import init_db
from library.services import (
    create_author,
    get_author_by_id,
    get_all_authors,
    update_author,
    delete_author
)
from demo_data import demo_authors

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
















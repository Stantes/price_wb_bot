import datetime
import re
import time

import openpyxl
from openpyxl.worksheet import worksheet

from dop_functions.parser import parse
from cfg.database import Database

db = Database('cfg/database')


def time_sub_day(get_time):
    time_now = int(time.time())
    middle_time = int(get_time) - time_now

    if middle_time <= 0:
        return False
    else:
        dt = str(datetime.timedelta(seconds=middle_time))
        dt = dt.replace("days", "дней")
        dt = dt.replace("day", "день")
        return dt


def days_to_secons(days):
    return days * 24 * 60 * 60


async def doc_exel(name, bot):
    i = 1
    filename = f"file/{name.from_user.id}.xlsx"
    book = openpyxl.load_workbook(filename=filename)
    sheet: worksheet = book["Лист1"]

    while True:
        count_add_products = len(db.get_add_tovar(name.chat.id))
        sub_count_products = db.get_sub_count_products(name.from_user.id)
        sub_count_products = int(re.search(r'\d+', str(sub_count_products))[0])

        if count_add_products < sub_count_products:
            art = sheet[f"A{i}"].value
            if art is None:
                break

            try:
                info_product = await parse(art)
                est = db.there_is_product(name.chat.id, art)

                if not est:
                    db.add_info_tovar(art, name.chat.id)

                    await bot.send_photo(name.chat.id, info_product[0], caption=f"""!!! Строка {i} записана !!!
    Название: {info_product[5]}
    Ссылка: {info_product[-1]}
    
    Цена Без скидки: {info_product[1]}руб
    Цена со скидкой: {info_product[2]}руб
    Цена с СПП: {info_product[4]}руб
    
    Артикул: {art}""")

                else:
                    # db.update_info_tovar(art, name.chat.id)
                    await bot.send_photo(name.chat.id, info_product[0], caption=f"""!!! Строка {i}, такой товар есть !!!
    Название: {info_product[5]}
    Ссылка: {info_product[-1]}
    
    Цена Без скидки: {info_product[1]}руб
    Цена со скидкой: {info_product[2]}руб
    Цена с СПП: {info_product[4]}руб
    
    Артикул: {art}""")

                in_products_table = db.there_is_in_roducts_table(art)
                if not in_products_table:
                    db.add_in_products_table(art, info_product[4])

            except:
                await name.answer(f"Строка {i} не записалась, такого товара нет")

            i += 1

        else:
            await name.answer("Добавлено максимальное количество товаров по вашей подписке!!")
            break

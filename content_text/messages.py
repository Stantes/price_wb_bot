from telegram_bot.utils import StatesSaveProducts

# СООБЩЕНИЯ ОТ БОТА
first_stat_message = """ добро пожаловать в Telegram бот от команды  CLUBBER 😎

Мы первые и единственные , кто отслеживает цены на Wildberries в реальном времени.
Мы будем улучшать бота и для нас важно твое мнение. 
Если есть пожелания или замечания по боту - напиши в поддержку: @CLUBBER_HELP """

second_stat_message = """Ну наконец-то, а мы думали, что уже не зайдешь!"""

help_message = """ ЛЮБУЮ ИНФОРМАЦИЮ """
about_the_project_message = """
Мы первые и единственные , кто отслеживает цены на Wildberries в реальном времени . Мы постоянно улучшаем бот и поэтому открыты для ваших пожеланий . 
В течении 3-х пробных дней вы можете оценить весь функционал бота и убедиться в его непрерывной работе . Рекомендуем использовать весь потенциал и добавлять максимальное допустимое количество товаров . И помни -  во вкладке "тарифы" это значение можно увеличить .
Если остались какие-то вопросы или нужна возможность отслеживать большее количество товаров - напиши в поддержку @CLUBBER_HELP
"""
referral_system_message = """
Ты будешь получать 30 % от платежей всех привлеченных тобой рефералов. Для приглашения используй реферальную ссылку: """
registered_by_ref_message = """ Вы зарегалимь по реф ссылке!! """
by_your_link_reg_message = """ По вашей ссылке зарегался новый пользователь """
you_cant_register_your_link_message = """ Нельзя регаться по своей ссылке """

subscription_description_message = "Выбери нужное количество товаров для парсинга"
cancellation_sub_message = "Подписка не оформленна, если нужна помощь - обратись в поддержку @CLUBBER_HELP"
cancellation_products_message = """Не забудь добавить товар для отслеживания!"""

subscription_buy_message =  "Вам выдана подписка!!!"
no_subscription_message = "Купите подписку, для возможности мониторинга цен!!!"
there_is_subscription_message = """Выберите функцию
    Добавить товар для мониторинга цены
    Посмотреть мои товары"""
add_product_message = """
-Что бы добавить один товар - пришли артикул товара
Пример: 349358493
- Что бы добавить несколько товаров - пришли Exel документ, в котором в столбце A находятся артиклы """
max_products_sub_message = "По вашей подписке добавлено максимальное количество товаров!!"
add_products_one_message = "Впиши артикул:"
add_products_more_message = "Отправь Exel файл"
there_is_product_message = "Товар добавлен!!!"
there_is_product_repeat_message = "Такой товар уже добавлен!!!"
update_price_products_message = "Такой товар есть!"
ne_tot_products_message = "Товар не добавлен!!!"
no_such_product_message = "Такого товара нет (("
there_is_exel_message = "Это Exel файл!"
not_exel_message = "Это не Exel файл!"
message_instead_of_file = "Нужно отправить Exel файл, а не сообщение("
no_added_products_messsage = "Нет добавленных товаров"
delete_product_message = "✔️ - оставить товар\n✖️ - удалить товар \n ❌ DEL ❌ - удалить все товары из списка"
delete_all_product_message = "Всё DELETE"

unknown_command_message = "Неизвестная команда пиши /start или /help"

MESSAGES = {
    "start": first_stat_message,
    "second_start": second_stat_message,

    "help": help_message,
    "about_the_project": about_the_project_message,
    "referral_system": referral_system_message,
    "registered_by_ref": registered_by_ref_message,
    "by_your_link_reg": by_your_link_reg_message,
    "you_cant_register_your_link": you_cant_register_your_link_message,
    "subscription_description": subscription_description_message,
    "cancellation_sub": cancellation_sub_message,
    "cancellation_products": cancellation_products_message,

    "subscription_buy": subscription_buy_message,
    "no_subscription": no_subscription_message,
    "there_is_subscription": there_is_subscription_message,
    "add_product": add_product_message,
    "max_products_sub": max_products_sub_message,
    "add_products_one_message": add_products_one_message,
    "add_products_more_message": add_products_more_message,
    "there_is_product": there_is_product_message,
    "there_is_product_repeat": there_is_product_repeat_message,
    "update_price_products": update_price_products_message,
    "ne_tot_products": ne_tot_products_message,
    "no_such_product": no_such_product_message,
    "there_is_exel": there_is_exel_message,
    "not_exel": not_exel_message,
    "message_instead_of_file": message_instead_of_file,
    "no_added_products": no_added_products_messsage,
    "delete_product": delete_product_message,
    "delete_all_product": delete_all_product_message,

    "unknown_command": unknown_command_message,
}

# СООБЩЕНИЯ ПРИ ОПЛАТЕ
name_subscription_1 = ""
name_subscription_2 = ""
name_subscription_3 = ""
name_subscription_4 = ""
# ЦЕНА ДЛЯ 10 ТОВАРОВ
price_1 = 29000
price_2 = 77900
price_3 = 147900
price_4 = 277900
# ЦЕНА ДЛЯ 50 ТОВАРОВ
price_5 = 49000
price_6 = 131900
price_7 = 249900
price_8 = 469900
# ЦЕНА ДЛЯ 100 ТОВАРОВ
price_9 = 79000
price_10 = 212900
price_11 = 402900
price_12 = 757900
# ЦЕНА ДЛЯ 500 ТОВАРОВ
price_13 = 109000
price_14 = 293900
price_15 = 555900
price_16 = 1045900


title_message = "Заголовок"
description_message = "Описание подписки"

MESSAGES_PAY = {
    "name_subscription_1": name_subscription_1,
    "name_subscription_2": name_subscription_2,
    "name_subscription_3": name_subscription_3,
    "name_subscription_4": name_subscription_4,
    "5": price_1,
    "6": price_2,
    "7": price_3,
    "8": price_4,

    "9": price_5,
    "10": price_6,
    "11": price_7,
    "12": price_8,

    "13": price_9,
    "14": price_10,
    "15": price_11,
    "16": price_12,

    "17": price_13,
    "18": price_14,
    "19": price_15,
    "20": price_16,

    "title": title_message,
    "description": description_message,
}

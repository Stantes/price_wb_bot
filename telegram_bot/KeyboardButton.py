from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# КНОПКИ МЕНЮ
btn_profile = KeyboardButton("Профиль")
btn_subscription = KeyboardButton("Подписка")
btn_products = KeyboardButton("Товары")
btn_info = KeyboardButton("О проекте")
btn_ref = KeyboardButton("Реферальная система")

# КНОПКИ ПОДПИСКИ КОЛ-ВО ТОВАРОВ
btn_type_of_subscription1 = InlineKeyboardButton(text="10 товаров", callback_data="10")
btn_type_of_subscription2 = InlineKeyboardButton(text="50 товаров", callback_data="50")
btn_type_of_subscription3 = InlineKeyboardButton(text="100 товаров", callback_data="100")
btn_type_of_subscription4 = InlineKeyboardButton(text="500 товаров", callback_data="500")
btn_cancellation = InlineKeyboardButton('✖️ Отмена ✖️', callback_data="cancellation")


# КНОПКА НАЗАД
btn_back = InlineKeyboardButton('🔙 Назад 🔙', callback_data="back")


# КНОПКИ ПОДПИСКИ КОЛ-ВО ВРЕМЕНИ ПРИ 10 ТОВАРАХ
btn_type_of_subscription_time_1 = InlineKeyboardButton(text="Месяц - 290р", callback_data="5")
btn_type_of_subscription_time_2 = InlineKeyboardButton(text="3 месяца - 779(-10%)", callback_data="6")
btn_type_of_subscription_time_3 = InlineKeyboardButton(text="6 месяцев - 1479(-15%)", callback_data="7")
btn_type_of_subscription_time_4 = InlineKeyboardButton(text="12 месяцев - 2779(-20%)", callback_data="8")

# КНОПКИ ПОДПИСКИ КОЛ-ВО ВРЕМЕНИ ПРИ 50 ТОВАРАХ
btn_type_of_subscription_time_5 = InlineKeyboardButton(text="Месяц - 490р", callback_data="9")
btn_type_of_subscription_time_6 = InlineKeyboardButton(text="3 месяца - 1319(-10%)", callback_data="10")
btn_type_of_subscription_time_7 = InlineKeyboardButton(text="6 месяцев - 2499(-15%)", callback_data="11")
btn_type_of_subscription_time_8 = InlineKeyboardButton(text="12 месяцев - 4699(-20%)", callback_data="12")

# КНОПКИ ПОДПИСКИ КОЛ-ВО ВРЕМЕНИ ПРИ 100 ТОВАРАХ
btn_type_of_subscription_time_9 = InlineKeyboardButton(text="Месяц - 790р", callback_data="13")
btn_type_of_subscription_time_10 = InlineKeyboardButton(text="3 месяца - 2129(-10%)", callback_data="14")
btn_type_of_subscription_time_11 = InlineKeyboardButton(text="6 месяцев - 4029(-15%)", callback_data="15")
btn_type_of_subscription_time_12 = InlineKeyboardButton(text="12 месяцев - 7579(-20%)", callback_data="16")

# КНОПКИ ПОДПИСКИ КОЛ-ВО ВРЕМЕНИ ПРИ 500 ТОВАРАХ
btn_type_of_subscription_time_13 = InlineKeyboardButton(text="Месяц - 1090р", callback_data="17")
btn_type_of_subscription_time_14 = InlineKeyboardButton(text="3 месяца - 2939(-10%)", callback_data="18")
btn_type_of_subscription_time_15 = InlineKeyboardButton(text="6 месяцев - 5559(-15%)", callback_data="19")
btn_type_of_subscription_time_16 = InlineKeyboardButton(text="12 месяцев - 10459(-20%)", callback_data="20")


# ДОБАВЛЕНИЕ / ПРОСМОТР ТОВАРОВ
btn_add_products = InlineKeyboardButton(text="Добавить товар", callback_data="add_products")
btn_views_produts = InlineKeyboardButton(text="Посмотреть добавленнные", callback_data="views_products")

# ДОБАВЛЕНИЕ ТОВАРА
btn_add_products_one = InlineKeyboardButton(text="Добавить один", callback_data="add_products_one")
btn_add_products_more = InlineKeyboardButton(text="Добавить несколько", callback_data="add_products_more")

# УДАЛИТЬ / ОСТАВИТ ДОБАВЛЕННЫЙ ТОВАР
btn_save_add_products = InlineKeyboardButton(text="✔️", callback_data="save_products")
btn_delete_add_products = InlineKeyboardButton(text="✖️", callback_data="delete_products")

# УДАЛИТЬ ВСЕ ТОВАРЫ
btn_delete_all_products = InlineKeyboardButton(text="❌ DEL ❌", callback_data="delete_all_products")

# ТОТ ТОВАР ИЛИ НЕТ
btn_tot_products = InlineKeyboardButton(text="✔️ Да ✔️", callback_data="tot_products")
btn_ne_tot_products = InlineKeyboardButton(text="✖️ Нет ✖️", callback_data="ne_tot_products")

BUTTON_TYPES = {
    "BTN_HOME": ReplyKeyboardMarkup(resize_keyboard=True).add(btn_profile, btn_subscription).add(btn_products).add(btn_info, btn_ref),
    "BTN_SUBSCRIPTIONS_PRICE": InlineKeyboardMarkup().add(btn_type_of_subscription1, btn_type_of_subscription2).add(
        btn_type_of_subscription3, btn_type_of_subscription4).add(btn_cancellation),

    "BTN_SUBSCRIPTIONS_PRICE_TIME_10": InlineKeyboardMarkup().add(btn_type_of_subscription_time_1, btn_type_of_subscription_time_2).add(
        btn_type_of_subscription_time_3, btn_type_of_subscription_time_4).add(btn_cancellation),

    "BTN_SUBSCRIPTIONS_PRICE_TIME_50": InlineKeyboardMarkup().add(btn_type_of_subscription_time_5,btn_type_of_subscription_time_6).add(
        btn_type_of_subscription_time_7, btn_type_of_subscription_time_8).add(btn_cancellation),

    "BTN_SUBSCRIPTIONS_PRICE_TIME_100": InlineKeyboardMarkup().add(btn_type_of_subscription_time_9,btn_type_of_subscription_time_10).add(
        btn_type_of_subscription_time_11, btn_type_of_subscription_time_12).add(btn_cancellation),

    "BTN_SUBSCRIPTIONS_PRICE_TIME_500": InlineKeyboardMarkup().add(btn_type_of_subscription_time_13,btn_type_of_subscription_time_14).add(
        btn_type_of_subscription_time_15, btn_type_of_subscription_time_16).add(btn_cancellation),

    'help': "",
    "BTN_CANCELLATION": InlineKeyboardMarkup().add(btn_cancellation),
    "BTN_ADD_VIEWS": InlineKeyboardMarkup().add(btn_add_products, btn_views_produts).add(btn_cancellation),
    "BTN_ADD_PRODUCTS": InlineKeyboardMarkup().add(btn_add_products_one, btn_add_products_more).add(btn_cancellation),
    "BTN_VIEWS_PRODUCTS": InlineKeyboardMarkup().add(btn_save_add_products, btn_delete_add_products),
    "BTN_DELETE_ALL_PRODUCTS": InlineKeyboardMarkup().add(btn_delete_all_products).add(btn_cancellation),
    "BTN_TOT_OR_NO": InlineKeyboardMarkup().add(btn_tot_products, btn_ne_tot_products),

    "BTN_BACK": InlineKeyboardMarkup().add(btn_back),
}

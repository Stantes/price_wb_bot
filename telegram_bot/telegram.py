import logging
import os
import time
import re

from aiogram import Bot, types
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, ContentTypes
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types.message import ContentType


from telegram_bot.utils import StatesSaveProducts
from content_text.messages import MESSAGES, MESSAGES_PAY
from telegram_bot.KeyboardButton import BUTTON_TYPES

from cfg.cfg import TOKEN, YOOPAYMENT, BOT_NICKNAME
from cfg.database import Database
from dop_functions.time_function import time_sub_day, days_to_secons, doc_exel
from dop_functions.parser import parse


db = Database('cfg/database')

logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

dp.middleware.setup(LoggingMiddleware())


# ===================================================
# =============== Стандартные команды ===============
# ===================================================
@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    if not db.user_exists(message.from_user.id):
        start_message = message.text
        referrer_id = str(start_message[7:])
        if referrer_id != "":
            if referrer_id != str(message.from_user.id):
                db.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, referrer_id)
                await message.answer(MESSAGES["registered_by_ref"])
                try:
                    await bot.send_message(referrer_id, MESSAGES["by_your_link_reg"])
                except:
                    pass
            else:
                db.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
                await message.answer(MESSAGES["you_cant_register_your_link"])
        else:
            db.add_user(message.from_user.id, message.from_user.username, message.from_user.first_name)

        await message.answer(f"{message.from_user.first_name}, {MESSAGES['start']}", reply_markup=BUTTON_TYPES["BTN_HOME"])
        time_sub = int(time.time()) + days_to_secons(3)
        db.set_time_sub(message.from_user.id, time_sub)
    else:
        await message.answer(f"Ну наконец-то {message.from_user.first_name}, а мы думали, что уже не зайдешь!", reply_markup=BUTTON_TYPES["BTN_HOME"])


@dp.message_handler(commands=['help'])
async def help_command(message: Message):
    await message.answer(MESSAGES['help'])


# ===================================================
# ===================== Buttons =====================
# ===================================================
@dp.message_handler(lambda message: message.text.lower() == 'профиль')
async def profile_info(message: Message):
    user_sub = time_sub_day(db.get_time_sub(message.from_user.id))
    sub_count_products = db.get_sub_count_products(message.from_user.id)
    sub_count_products = re.search(r'\d+', str(sub_count_products))[0]
    count_products_user = len(db.get_add_tovar(message.chat.id))

    if not user_sub:
        user_sub = "Подписки нет!!!"
        sub_count_products = 0

    await message.answer(f"""Ваш ник: {message.from_user.username}
Подписка: {user_sub}
MAX количество товаров для парсинга: {sub_count_products} 
Добавленно товаров: {count_products_user}""")


@dp.message_handler(lambda message: message.text.lower() == 'подписка')
async def types_of_subscriptions(message: Message):
    await message.answer(MESSAGES["subscription_description"], reply_markup=BUTTON_TYPES["BTN_SUBSCRIPTIONS_PRICE"])


@dp.message_handler(lambda message: message.text.lower() == 'товары')
async def product_btn(message: Message):
    if db.get_sub_status(message.from_user.id):
        await bot.send_message(message.from_user.id, MESSAGES["there_is_subscription"], reply_markup=BUTTON_TYPES["BTN_ADD_VIEWS"])
    else:
        await bot.send_message(message.from_user.id, MESSAGES["no_subscription"])


@dp.message_handler(lambda message: message.text.lower() == "о проекте")
async def types_of_subscriptions(message: Message):
    await message.answer(MESSAGES["about_the_project"], reply_markup=BUTTON_TYPES["BTN_HOME"])


@dp.message_handler(lambda message: message.text.lower() == "реферальная система")
async def types_of_subscriptions(message: Message):
    await message.answer(f"""{MESSAGES['referral_system']}
    
https://t.me/{BOT_NICKNAME}?start={message.from_user.id} 
Кол-во рефералов: {db.count_referrals(message.from_user.id)}""", reply_markup=BUTTON_TYPES["BTN_HOME"])

# ===================================================
# ================= Покупка подписки ================
# ===================================================
@dp.callback_query_handler(lambda c: c.data == "10" or c.data == "50" or c.data == "100" or c.data == "500")
async def buy_subscriptions(callback: CallbackQuery):
    if int(db.count_referrals(callback.from_user.id)) < 3:
        # Нет скидки
        discount = "0%"
    elif int(db.count_referrals(callback.from_user.id)) < 6:
        # Скидка 10%
        discount = "10%"
    elif int(db.count_referrals(callback.from_user.id)) < 9:
        # Скидка 20%
        discount = "20%"
    else:
        # Скидка 30%
        discount = "30%"

    await callback.message.edit_text(f"Выбери на какое время подписка для {callback.data} товаров \n Твоя скидка составляет: {discount}")
    await callback.message.edit_reply_markup(reply_markup=BUTTON_TYPES[f"BTN_SUBSCRIPTIONS_PRICE_TIME_{callback.data}"])



@dp.callback_query_handler(lambda c: c.data == "5" or c.data == "6" or c.data == "7" or c.data == "8" or c.data == "9" or c.data == "10" or c.data == "11"
or c.data == "12" or c.data == "13" or c.data == "14" or c.data == "15" or c.data == "16"  or c.data == "17" or c.data == "18" or c.data == "19" or c.data == "20")
async def buy_subscriptions(callback: CallbackQuery):
    if int(db.count_referrals(callback.from_user.id)) < 3:
        discount = 1
    elif int(db.count_referrals(callback.from_user.id)) < 6:
        discount = 0.9
    elif int(db.count_referrals(callback.from_user.id)) < 9:
        discount = 0.8
    else:
        discount = 0.7

    label = "Описание"

    PRICE = types.LabeledPrice(label=label, amount=int(MESSAGES_PAY[f"{callback.data}"] * discount))
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    await bot.send_invoice(
        chat_id=callback.message.chat.id,
        title=MESSAGES_PAY["title"],
        description=MESSAGES_PAY["description"],
        provider_token=YOOPAYMENT,
        currency='RUB',
        prices=[PRICE],
        start_parameter='time-machine-example',
        payload=f"{callback.data}",
    )

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: Message):
    payload_name = message.successful_payment.invoice_payload
    time_sub = 0

    # Добавление кол-ва товаров
    if payload_name == "5" or payload_name == "6" or payload_name == "7" or payload_name == "8":
        db.add_sub_count_producs(message.from_user.id, 10)
    if payload_name == "9" or payload_name == "10" or payload_name == "11" or payload_name == "12":
        db.add_sub_count_producs(message.from_user.id, 50)
    if payload_name == "13" or payload_name == "14" or payload_name == "15" or payload_name == "16":
        db.add_sub_count_producs(message.from_user.id, 100)
    if payload_name == "17" or payload_name == "18" or payload_name == "19" or payload_name == "20":
        db.add_sub_count_producs(message.from_user.id, 500)

    # Добавление времени
    if payload_name == "5" or payload_name == "9" or payload_name == "13" or payload_name == "17":
        time_sub = int(time.time()) + days_to_secons(30)
    if payload_name == "6" or payload_name == "10" or payload_name == "14" or payload_name == "18":
        time_sub = int(time.time()) + days_to_secons(90)
    if payload_name == "7" or payload_name == "11" or payload_name == "15" or payload_name == "19":
        time_sub = int(time.time()) + days_to_secons(180)
    if payload_name == "8" or payload_name == "12" or payload_name == "16" or payload_name == "20":
        time_sub = int(time.time()) + days_to_secons(360)

    db.set_time_sub(message.from_user.id, time_sub)

    await bot.send_message(message.from_user.id, MESSAGES["subscription_buy"])



# ===================================================
# ================= Добавление Товара ===============
# ===================================================
@dp.callback_query_handler(lambda c: c.data == "add_products")
async def type_of_add(callback: CallbackQuery):
    count_add_products = len(db.get_add_tovar(callback.message.chat.id))
    sub_count_products = db.get_sub_count_products(callback.from_user.id)
    sub_count_products = int(re.search(r'\d+', str(sub_count_products))[0])

    if count_add_products < sub_count_products:
        await callback.message.edit_text(MESSAGES["add_product"])
        await callback.message.edit_reply_markup(reply_markup=BUTTON_TYPES["BTN_ADD_PRODUCTS"])
    else:
        await callback.message.edit_text(MESSAGES["max_products_sub"])

# ================= Добавление одного ===============
@dp.callback_query_handler(lambda c: c.data == "add_products_one")
async def data_add_one(callback: CallbackQuery):
    await callback.message.edit_text(MESSAGES["add_products_one_message"])
    await callback.message.edit_reply_markup(reply_markup=BUTTON_TYPES["BTN_BACK"])

    state = dp.current_state(user=callback.from_user.id)
    await state.set_state(StatesSaveProducts.all()[1])


# =================== НАЗАД =======================
@dp.callback_query_handler(lambda c: c.data == "back", state=StatesSaveProducts.STATE_ADD_ONE | StatesSaveProducts.STATE_ADD_MORE)
async def back(callback: CallbackQuery):
    count_add_products = len(db.get_add_tovar(callback.message.chat.id))
    sub_count_products = db.get_sub_count_products(callback.from_user.id)
    sub_count_products = int(re.search(r'\d+', str(sub_count_products))[0])

    if count_add_products < sub_count_products:
        await callback.message.edit_text(MESSAGES["add_product"])
        await callback.message.edit_reply_markup(reply_markup=BUTTON_TYPES["BTN_ADD_PRODUCTS"])
    else:
        await callback.message.edit_text(MESSAGES["max_products_sub"])

    state = dp.current_state(user=callback.from_user.id)
    await state.reset_state(with_data=False)



# ================= Тот Или Не Тот =================
@dp.message_handler(state=StatesSaveProducts.STATE_ADD_ONE)
async def add_one(message: Message, state: FSMContext):
    try:
        art = int(message.text)
        info_product = await parse(art)

        await state.update_data(art=art)
        await state.update_data(price_spp=info_product[4])

        state = dp.current_state(user=message.from_user.id)
        await bot.send_photo(message.chat.id, info_product[0], reply_markup=BUTTON_TYPES["BTN_TOT_OR_NO"],
                             caption=f"""Вы искали этот товар?
                             
Название: {info_product[5]}
Ссылка: {info_product[-1]}

Цена Без скидки: {info_product[1]}руб
Цена со скидкой: {info_product[2]}руб
Цена с СПП: {info_product[4]}руб

Артикул: {art}
""")
        await state.set_state(StatesSaveProducts.all()[2])

    except:
        await message.answer(MESSAGES["no_such_product"], reply_markup=BUTTON_TYPES["BTN_HOME"])
        await state.reset_state(with_data=False)


# ===================== Тот Товар ======================
@dp.callback_query_handler(state=StatesSaveProducts.STATE_ADD_ONE_1)
async def type_of_add(callback: CallbackQuery):
    state = dp.current_state(user=callback.from_user.id)

    if callback.data == "tot_products":
        data = await state.get_data()
        art = data["art"]
        price_spp = data["price_spp"]

        est = db.there_is_product(callback.message.chat.id, art)
        await callback.message.edit_reply_markup()

        if not est:
            db.add_info_tovar(art, callback.message.chat.id)
            await callback.message.answer(MESSAGES["there_is_product"], reply_markup=BUTTON_TYPES["BTN_HOME"])
        else:
            await callback.message.answer(MESSAGES["there_is_product_repeat"], reply_markup=BUTTON_TYPES["BTN_HOME"])
        in_products_table = db.there_is_in_roducts_table(art)

        if not in_products_table:
            db.add_in_products_table(art, price_spp)


    elif callback.data == "ne_tot_products":
        await callback.message.edit_reply_markup()
        await callback.message.answer(MESSAGES["ne_tot_products"], reply_markup=BUTTON_TYPES["BTN_HOME"])

    await state.reset_state(with_data=False)

# ================= Добавление Нескольких ===============
@dp.callback_query_handler(lambda c: c.data == "add_products_more")
async def file_add_more(callback: CallbackQuery):
    await callback.message.edit_text(MESSAGES["add_products_more_message"])
    await callback.message.edit_reply_markup(reply_markup=BUTTON_TYPES["BTN_BACK"])


    state = dp.current_state(user=callback.from_user.id)
    await state.set_state(StatesSaveProducts.all()[0])


@dp.message_handler(content_types=ContentTypes.DOCUMENT, state=StatesSaveProducts.STATE_ADD_MORE)
async def add_more(message: Message):
    if ".xlsx" in message.document.file_name:
        if document := message.document:
            await document.download(
                destination_file=f"file/{message.from_user.id}.xlsx",
            )

        await doc_exel(message, bot)

        await message.answer(MESSAGES["there_is_exel"], reply_markup=BUTTON_TYPES["BTN_HOME"])
        os.remove(f"file/{message.from_user.id}.xlsx")

    else:
        await message.answer(MESSAGES["not_exel"],  reply_markup=BUTTON_TYPES["BTN_HOME"])

    state = dp.current_state(user=message.from_user.id)
    await state.reset_state(with_data=False)

# =================== Если вместо файла отправили сообщение ===================
@dp.message_handler(state=StatesSaveProducts.STATE_ADD_MORE)
async def add_more(message: Message):
    await message.answer(MESSAGES["message_instead_of_file"],  reply_markup=BUTTON_TYPES["BTN_HOME"])
    state = dp.current_state(user=message.from_user.id)
    await state.reset_state(with_data=False)


# ===================================================
# ================== Просмотр Товара ================
# ===================================================
@dp.callback_query_handler(lambda c: c.data == "views_products")
async def views_products(callback: CallbackQuery):
    await callback.message.delete()
    get_tovat_art_price = db.get_add_tovar(callback.from_user.id)

    if not get_tovat_art_price:
        await callback.message.answer(MESSAGES["no_added_products"])

    else:
        for art_price in get_tovat_art_price:
            art = re.sub(r'\(', '', str(art_price))
            art = re.sub(r',\)', '', str(art))


            info_product = await parse(int(art))

            await bot.send_photo(callback.message.chat.id, info_product[0], caption=f"""Название: {info_product[5]}
Ссылка: {info_product[-1]}

Артикул: {art}""", reply_markup=BUTTON_TYPES["BTN_VIEWS_PRODUCTS"])

        await callback.message.answer(MESSAGES["delete_product"], reply_markup=BUTTON_TYPES["BTN_DELETE_ALL_PRODUCTS"])

    await callback.answer()

# ================== Оставить Товар ================
@dp.callback_query_handler(lambda c: c.data == "save_products")
async def save_products(callback: CallbackQuery):
    await callback.message.edit_reply_markup()

# ================== Удалить Товар ================
@dp.callback_query_handler(lambda c: c.data == "delete_products")
async def delete_products(callback: CallbackQuery):
    art = re.search(r'Артикул: \d+', str(callback.message.caption))[0]
    art = re.sub(r'Артикул: ', '', art)

    await callback.message.edit_reply_markup()
    await callback.message.edit_caption(f"{callback.message.caption}\n\n  ❌ Товар удалён ❌")
    db.delete_tovar(art, callback.message.chat.id)
    get_all_art = db.get_all_users_art(art)

    if get_all_art == []:
        db.delete_tovar_in_products_table(art)

    await callback.answer()

# ==================== Удалить Все Товар ==================
@dp.callback_query_handler(lambda c: c.data == "delete_all_products")
async def delete_all_products(callback: CallbackQuery):
    await callback.message.edit_reply_markup()
    await callback.message.edit_text(MESSAGES["delete_all_product"])

    all_art = db.get_all_art_users(callback.from_user.id)
    db.delete_all_tovar(callback.from_user.id)

    for art in all_art:
        art = int(re.search(r'\d+', str(art))[0])

        get_all_art = db.get_all_users_art(art)
        if get_all_art == []:
            db.delete_tovar_in_products_table(art)

    await callback.answer()


# ===================== Кнопка отмены =====================
@dp.callback_query_handler(lambda c: c.data == 'cancellation')
async def cancellation_inline(callback: CallbackQuery):

    await callback.message.edit_reply_markup()
    if callback.message.text == MESSAGES["there_is_subscription"] or callback.message.text == MESSAGES["add_product"]:
        await callback.message.edit_text(MESSAGES["cancellation_products"])

    elif callback.message.text == MESSAGES["subscription_description"] or "Выбери на какое время подписка для" in callback.message.text:
        await callback.message.edit_text(MESSAGES["cancellation_sub"])

    await callback.answer()

# ===================== Неизвестная команда =====================
@dp.message_handler()
async def unknown_command(message: Message):
    await message.answer(MESSAGES["unknown_command"])


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


def start():
    executor.start_polling(dp, on_shutdown=shutdown)

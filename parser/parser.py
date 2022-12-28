from db import Database
from time import sleep
import requests
from mpire import WorkerPool

db = Database('../cfg/database')

cookies = {
    '___wbu': 'b6ca5c30-4793-4326-b894-3f7f0407b166.1669911458',
    '__pricemargin': '1.0--',
    '__sppfix': '4',
    '__store': '117673_122258_122259_125238_125239_125240_507_3158_117501_120602_120762_6158_121709_124731_130744_159402_2737_117986_1733_686_132043_161812_1193_206968_206348_205228_172430_117442_117866',
    '_wbauid': '7370590681669911458',
    'BasketUID': 'a2f00653-442b-4085-bf8d-84eaf3f41467',
    '__wba_s': '1',
    'WILDAUTHNEW_V3': '0247725265F619122B725BAE3E7C13E36836907C8530C53D43894F36267C4D274C5700483346B405DD6388B19C9DD633B415423353A7C0225487F17EE68BC009CC132AEC7687F8BA4D6C21B797EDA4140A39B20137F682D0ADA0A50665AB95105EC696E36E87FB499DC706F51E59F7CF16F0DC7AE856D25410C32CB5A3DD66B5CAAB1CB193BAD171A5E17CE423A1D0C12EEA705DD8A76913E6EDEE0B155BA3058E4DD09623F9656FEA61E0764A98D1E83489B23E063386689D04000DBD6C206DDEB427D0467E5D64404A6DE3F400CB595CF265F942295F76D412C22C191663CD46B7108D4686B5F9E280A6D3EE06305B49D913ACA65D5189A49D1049672128C2F73DA531EB76320BED2B29CA9DBC01019F28FA7356E2F6854BB13CA570152725376579D5',
    '__wbl': 'cityId%3D0%26regionId%3D0%26city%3D%D0%B3.%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%BC%20%D0%90%D1%80%D0%B1%D0%B0%D1%82%D1%81%D0%BA%D0%B0%D1%8F%20%28%D0%90%D1%80%D0%B1%2F%D0%9F%D0%BE%D0%BA%D1%80%29%2C%20%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9%20%D0%90%D1%84%D0%B0%D0%BD%D0%B0%D1%81%D1%8C%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%B5%D1%80%D0%B5%D1%83%D0%BB%D0%BE%D0%BA%2C%20%D0%B4.%2022%26phone%3D84957755505%26latitude%3D55%2C748858000%26longitude%3D37%2C597414000%26src%3D1',
    '__region': '80_64_83_4_38_33_70_82_69_68_86_75_30_40_48_1_22_66_31_71',
    '__cpns': '12_3_18_15_21',
    '__dst': '-1029256_-102269_-2162196_-1257484',
    'ncache': '117673_122258_122259_125238_125239_125240_507_3158_117501_120602_120762_6158_121709_124731_130744_159402_2737_117986_1733_686_132043_161812_1193_206968_206348_205228_172430_117442_117866%3B80_64_83_4_38_33_70_82_69_68_86_75_30_40_48_1_22_66_31_71%3B1.0--%3B12_3_18_15_21%3B4%3B-1029256_-102269_-2162196_-1257484',
    '_wbSes': 'CfDJ8OvUqgYvh81KnUmy154niGFcOcElydXPanFZP68HlrTNsXYkaxDjw1%2FhOdJ160pyN2J6KlSx8A4m6yantSQP1N3m8BX9hYJUsx1SJNu%2FaA8K%2BGRY%2BQ0PXudU0gQnlDJM2%2B4oWEk2cGQULdRZsKKXI7jhjbpYlFV7WCVF%2BHHVfRt5',
    '__bsa': 'basket-ru-38',
    'um': 'uid%3Dw7TDssOkw7PCu8K3wrLCssK1wrPCsMK2wrU%253d%3Aproc%3D100%3Aehash%3Dd41d8cd98f00b204e9800998ecf8427e',
    '__tm': '1670520012',
}

headers = {
    'authority': 'www.wildberries.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'content-length': '0',
    # 'cookie': '___wbu=b6ca5c30-4793-4326-b894-3f7f0407b166.1669911458; __pricemargin=1.0--; __sppfix=4; __store=117673_122258_122259_125238_125239_125240_507_3158_117501_120602_120762_6158_121709_124731_130744_159402_2737_117986_1733_686_132043_161812_1193_206968_206348_205228_172430_117442_117866; _wbauid=7370590681669911458; BasketUID=a2f00653-442b-4085-bf8d-84eaf3f41467; __wba_s=1; WILDAUTHNEW_V3=0247725265F619122B725BAE3E7C13E36836907C8530C53D43894F36267C4D274C5700483346B405DD6388B19C9DD633B415423353A7C0225487F17EE68BC009CC132AEC7687F8BA4D6C21B797EDA4140A39B20137F682D0ADA0A50665AB95105EC696E36E87FB499DC706F51E59F7CF16F0DC7AE856D25410C32CB5A3DD66B5CAAB1CB193BAD171A5E17CE423A1D0C12EEA705DD8A76913E6EDEE0B155BA3058E4DD09623F9656FEA61E0764A98D1E83489B23E063386689D04000DBD6C206DDEB427D0467E5D64404A6DE3F400CB595CF265F942295F76D412C22C191663CD46B7108D4686B5F9E280A6D3EE06305B49D913ACA65D5189A49D1049672128C2F73DA531EB76320BED2B29CA9DBC01019F28FA7356E2F6854BB13CA570152725376579D5; __wbl=cityId%3D0%26regionId%3D0%26city%3D%D0%B3.%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%BC%20%D0%90%D1%80%D0%B1%D0%B0%D1%82%D1%81%D0%BA%D0%B0%D1%8F%20%28%D0%90%D1%80%D0%B1%2F%D0%9F%D0%BE%D0%BA%D1%80%29%2C%20%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9%20%D0%90%D1%84%D0%B0%D0%BD%D0%B0%D1%81%D1%8C%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%B5%D1%80%D0%B5%D1%83%D0%BB%D0%BE%D0%BA%2C%20%D0%B4.%2022%26phone%3D84957755505%26latitude%3D55%2C748858000%26longitude%3D37%2C597414000%26src%3D1; __region=80_64_83_4_38_33_70_82_69_68_86_75_30_40_48_1_22_66_31_71; __cpns=12_3_18_15_21; __dst=-1029256_-102269_-2162196_-1257484; ncache=117673_122258_122259_125238_125239_125240_507_3158_117501_120602_120762_6158_121709_124731_130744_159402_2737_117986_1733_686_132043_161812_1193_206968_206348_205228_172430_117442_117866%3B80_64_83_4_38_33_70_82_69_68_86_75_30_40_48_1_22_66_31_71%3B1.0--%3B12_3_18_15_21%3B4%3B-1029256_-102269_-2162196_-1257484; _wbSes=CfDJ8OvUqgYvh81KnUmy154niGFcOcElydXPanFZP68HlrTNsXYkaxDjw1%2FhOdJ160pyN2J6KlSx8A4m6yantSQP1N3m8BX9hYJUsx1SJNu%2FaA8K%2BGRY%2BQ0PXudU0gQnlDJM2%2B4oWEk2cGQULdRZsKKXI7jhjbpYlFV7WCVF%2BHHVfRt5; __bsa=basket-ru-38; um=uid%3Dw7TDssOkw7PCu8K3wrLCssK1wrPCsMK2wrU%253d%3Aproc%3D100%3Aehash%3Dd41d8cd98f00b204e9800998ecf8427e; __tm=1670520012',
    'dnt': '1',
    'origin': 'https://www.wildberries.ru',
    'referer': 'https://www.wildberries.ru/catalog/104879483/detail.aspx?targetUrl=MI',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '9.3.68',
}
session = requests.Session()
session.cookies.update(cookies)
session.headers.update(headers)


# Получаем адрес типа https://basket-01.wb.ru/
def get_basket(article):
    # //basket-05.wb.ru/vol981/part98157/98157706/images/big/1.jpg
    vol = int(article / 100000)
    part = int(article / 1000)
    if 0 <= vol <= 143:
        basket = f'https://basket-01.wb.ru/vol{vol}/part{part}/{article}'
    elif 144 <= vol <= 287:
        basket = f'https://basket-02.wb.ru/vol{vol}/part{part}/{article}'
    elif 288 <= vol <= 431:
        basket = f'https://basket-03.wb.ru/vol{vol}/part{part}/{article}'
    elif 432 <= vol <= 719:
        basket = f'https://basket-04.wb.ru/vol{vol}/part{part}/{article}'
    elif 720 <= vol <= 1007:
        basket = f'https://basket-05.wb.ru/vol{vol}/part{part}/{article}'
    elif 1008 <= vol <= 1061:
        basket = f'https://basket-06.wb.ru/vol{vol}/part{part}/{article}'
    elif 1062 <= vol <= 1115:
        basket = f'https://basket-07.wb.ru/vol{vol}/part{part}/{article}'
    elif 1116 <= vol <= 1169:
        basket = f'https://basket-08.wb.ru/vol{vol}/part{part}/{article}'
    elif 1170 <= vol <= 1313:
        basket = f'https://basket-09.wb.ru/vol{vol}/part{part}/{article}'
    elif 1314 <= vol <= 1601:
        basket = f'https://basket-10.wb.ru/vol{vol}/part{part}/{article}'
    else:
        basket = f'https://basket-11.wb.ru/vol{vol}/part{part}/{article}'

    return basket


# Получает цены
def get_product_price(*data):
    article = int(data[0])
    old_price = int(data[1])
    response = session.post('https://www.wildberries.ru/webapi/user/get-xinfo-v2')
    url = f'https://card.wb.ru/cards/detail?{response.json()["xinfo"]}&nm={article}'
    data = session.get(url).json()

    try:
        sale = int(data['data']['products'][0]['extended']['basicPriceU'] / 100)
    except:
        sale = int(data['data']['products'][0]['salePriceU'] / 100)

    try:
        client_sale = int(data['data']['products'][0]['extended']['clientSale'])  # Если есть скидка СПП %
        sale_spp = int(data['data']['products'][0]['extended']['clientPriceU'] / 100) # Цена со скидкой СПП
    except:
        client_sale = 0
        sale_spp = 0

    # return sale_spp if sale_spp > 0 else sale
    if sale_spp > 0 and sale_spp != int(old_price):
        # Получаем пользователей, которые мониторят данный товар
        users = db.get_users_products(article)
        for chat_id in users:
            send_user_new_price(chat_id[0], article, old_price, sale_spp) # Отправляем пользователю новую цену с СПП
        # Обновляем цену товара в базе на текущую
        db.update_product_price(article, sale_spp)

    if sale_spp == 0 and sale != int(old_price):
        # Получаем пользователей, которые мониторят данный товар
        users = db.get_users_products(article)
        for chat_id in users:
            send_user_new_price(chat_id[0], article, old_price, sale)  # Отправляем пользователю новую цену с обычной скидкой
        # Обновляем цену товара в базе на текущую
        db.update_product_price(article, sale)


# Отправляем пользователям уведомление
def send_user_new_price(chat_id, article, old_price, new_price):
    # Проверяем, есть ли у пользователя подписка
    if db.get_sub_status(chat_id):
        # Если есть, отправляем новую цену на товар
        basket = get_basket(article)
        # print(basket)
        caption = f"""
Цена товара изменилась!!!
Ссылка: https://www.wildberries.ru/catalog/{article}/detail.aspx
Артикул: {article}
Была: {old_price}
Стала: {new_price}
"""
        # Оправляем картинку товара и данные по бывшей и текущей цене
        data = f'https://api.telegram.org/bot5697948615:AAF_sDFw7P-7CwQ-mx3eVzjDWT5Mh5P04tQ/sendPhoto?' \
               f'chat_id={chat_id}' \
               f'&photo={basket}/images/big/1.jpg&' \
               f'caption={caption}'
        requests.get(data)


def main():
    while True:
        # Выбираем все товары из таблицы базы products
        products = db.get_all_products()

        # Парсим текущую цену товара и, при ее изменеии, отправляем пользователям сообщение
        with WorkerPool(n_jobs=50) as p:
            p.map(get_product_price, products)

        sleep(10)


if __name__ == '__main__':
    main()

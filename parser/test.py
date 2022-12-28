import sqlite3
import requests
connection = sqlite3.connect('../cfg/database')
cursor = connection.cursor()
def user_exists():
	with connection:
	    result = cursor.execute("SELECT user_id FROM `users`").fetchall()
	    return result

for i in user_exists():
    url = f"https://api.telegram.org/bot5697948615:AAF_sDFw7P-7CwQ-mx3eVzjDWT5Mh5P04tQ/sendMessage?chat_id={i[0]}&parse_mode=html&text=Добрый день. По техническим причинам бот не работал. Сейчас бот полностью функционирует, можете пользоваться. Пробные периоды обновили."
    requests.get(url)

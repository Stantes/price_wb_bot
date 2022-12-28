import sqlite3
import time

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get_sub_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            if time_sub > int(time.time()):
                return True
            else:
                return False

    def get_all_products(self):
        with self.connection:
            result = self.cursor.execute("SELECT art, price_spp FROM `products`").fetchall()
            return result

    def get_users_products(self, prod_id):
        with self.connection:
            result = self.cursor.execute("SELECT id_chat FROM `users_products` WHERE `art` = ?", (prod_id,)).fetchall()
            return result

    def update_product_price(self, article, price):
        with self.connection:
            return self.cursor.execute("UPDATE `products` SET `price_spp` = ? WHERE `art` = ?", (price, article,))

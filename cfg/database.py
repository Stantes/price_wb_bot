import sqlite3
import time

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, usernme, nickname, reffere_id=None):
        with self.connection:
            if reffere_id is not None:
                return self.cursor.execute("INSERT INTO `users` (`user_id`, `nickname`, `signup`, `referrer_id`) VALUES (?, ?, ?, ?)", (user_id, usernme, nickname, reffere_id,))
            else:
                return self.cursor.execute("INSERT INTO `users` (`user_id`, `nickname`, `signup`) VALUES (?, ?, ?)", (user_id, usernme, nickname,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `nickname` = ? WHERE `user_id` = ?", (nickname, user_id,))

    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `user_id` = ?", (signup, user_id,))

    def get_nickname(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `nickname` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                nickname = str(row[0])
            return nickname

    def set_time_sub(self, user_id, time_sub):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `time_sub` = ? WHERE `user_id` = ?", (time_sub, user_id,))

    def get_time_sub(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            return time_sub

    def get_sub_status(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `time_sub` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                time_sub = int(row[0])
            if time_sub > int(time.time()):
                return True
            else:
                return False


    def add_info_tovar(self, art, id_chat):
        with self.connection:
            return self.cursor.execute(f"""INSERT INTO users_products (art, id_chat) VALUES ({art}, {id_chat});""")

    def get_add_tovar(self, id_chat):
        with self.connection:
            result = self.cursor.execute("SELECT `art` FROM `users_products` WHERE `id_chat` = ?", (id_chat,)).fetchall()
            return result

    def delete_tovar(self, art, id_chat):
        with self.connection:
            result = self.cursor.execute("DELETE FROM `users_products` WHERE `art` = ? and `id_chat` = ?", (art, id_chat)).fetchall()
            return result

    def delete_all_tovar(self, id_chat):
        with self.connection:
            result = self.cursor.execute("DELETE FROM `users_products` WHERE `id_chat` = ?", (id_chat,)).fetchall()
            return result

    def there_is_product(self, id_chat, art):
        with self.connection:
            result = self.cursor.execute("SELECT `art` FROM `users_products` WHERE `id_chat` = ? and `art` = ?", (id_chat, art)).fetchall()
            return result

    def there_is_in_roducts_table(self, art):
        with self.connection:
            result = self.cursor.execute("SELECT `art` FROM `products` WHERE `art` = ?", (art,)).fetchall()
            return result

    def add_in_products_table(self, art, price_spp):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO products (art, price_spp) VALUES ({art}, {price_spp});")

    def add_sub_count_producs(self, user_id, number_of_products):
        with self.connection:
            return self.cursor.execute(f"UPDATE users SET number_of_products = {number_of_products} WHERE user_id = {user_id};")

    def get_sub_count_products(self, user_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT `number_of_products` FROM `users` WHERE `user_id` = {user_id}").fetchall()
            return result

    def get_all_users_art(self, art):
        with self.connection:
            result = self.cursor.execute(f"SELECT `id_chat` FROM `users_products` WHERE `art` = {art}").fetchall()
            return result

    def delete_tovar_in_products_table(self, art):
        with self.connection:
            result = self.cursor.execute("DELETE FROM `products` WHERE `art` = ?", (art,)).fetchall()
            return result

    def get_all_art_users(self, user_id):
        with self.connection:
            result = self.cursor.execute(f"SELECT `art` FROM `users_products` WHERE `id_chat` = {user_id}").fetchall()
            return result

    def count_referrals(self, user_id):
        with self.connection:
            return self.cursor.execute("SELECT COUNT (`id`) as count FROM `users` WHERE `referrer_id` = ?", (user_id,)).fetchone()[0]
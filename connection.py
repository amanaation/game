import mysql.connector


class Connection:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="aman",
            password="Aman@123",
            database="game"
        )
        self.cur = self.conn.cursor()

    def get_user(self):
        pass

    def add_user(self, user_name, code):
        query = f"""Insert into user(user_name) values('{user_name}');"""
        print(self.cur.execute(query))
        print(self.cur.execute("Commit;"))

        user_id = self.get_user_id(user_name)
        res = self.add_user_game(user_id, code)
        return res

    def get_score(self):
        pass

    def get_code_id(self):
        query = "Select game_id from game_code where code = 'ABCD'";
        self.cur.execute(query)
        res = self.cur.fetchall()
        print(res)

    def get_user_id(self, name):
        query = f"Select user_id from user where name = '{name}'"
        self.cur.execute(query)
        res = self.cur.fetchall()
        return res[0][0]

    def add_user_game(self, user_id, code):
        try:
            query = f"Insert into user_game_mapping values('{user_id}', '{code}');"
            return "Added User Successfully"
        except:
            return "Failed to add user"


# if __name__ == "__main__":
#     Connection().get_code_id()

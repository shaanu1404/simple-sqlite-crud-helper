import sqlite3



class Database:

    def __init__(self, columns):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()

        col_list = []
        for name, attr in columns.items():
            col_str = "{} {}".format(name, " ".join(attr))
            col_list.append(col_str)
        col = ", ".join(col_list)

        sql = """CREATE TABLE IF NOT EXISTS {table}(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {col}
        )""".format(table=self.table, col=col)

        try:
            self.cursor.execute(sql)
            print('%s table created successfully' % self.table)
        except Exception as e:
            print(e)

    def fetch_one(self, **column):
        col_name = tuple(column)[0]
        value = column[col_name]

        sql = """SELECT * FROM {}""".format(self.table)
        if isinstance(value, int):
            sql = """SELECT * FROM {} WHERE {} = {}""".format(
                self.table, col_name, value)
        elif isinstance(value, str):
            sql = """SELECT * FROM {} WHERE {} LIKE '%{}%'""".format(
                self.table, col_name, value)

        try:
            self.cursor.execute(sql)
            obj = self.cursor.fetchone()
            return obj
        except Exception as e:
            print(e)

    def fetch_all(self):
        sql = """SELECT * FROM {}""".format(self.table)

        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(e)

    def fetch_columns(self, columns=[], lookup=""):
        col_str = "*"
        if len(columns) > 0:
            col_str = ", ".join(columns)
        sql = f"SELECT {col_str} FROM {self.table}"

        if lookup:
            sql += f" WHERE {lookup}"

        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            return rows
        except Exception as e:
            print(e)

    def insert(self, data):
        col_names = list(data)
        if len(col_names) <= 0:
            return False
        cols_str = ", ".join(col_names)
        qmarks = ", ".join(['?' for i in range(len(col_names))])
        sql = """INSERT INTO {}({}) VALUES({})""".format(
            self.table, cols_str, qmarks)
        values = [data[col] for col in col_names]
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, lookup):
        sql = f"DELETE FROM {self.table} WHERE {lookup}"
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, lookup, data):
        if len(data) <= 0:
            return False
        data_keys = [f"{i} = ?" for i in data]
        data_keys_str = ", ".join(data_keys)
        values = [data[col] for col in data]
        sql = f"UPDATE {self.table} SET {data_keys_str} WHERE {lookup}"
        try:
            self.cursor.execute(sql, values)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
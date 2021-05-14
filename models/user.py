from database import Database


class User(Database):

    table = 'users'

    def __init__(self):
        super().__init__(columns={
            "name": ('TEXT', 'NOT NULL'),
            "email": ('TEXT', 'NOT NULL'),
        })

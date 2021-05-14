from database import Database


class Product(Database):

    table = 'products'

    def __init__(self):
        super().__init__(columns={
            "title": ('TEXT', 'NOT NULL'),
            "description": ('TEXT', 'NULL'),
            "price": ("INTEGER", "NOT NULL")
        })

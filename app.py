from models.user import User
from models.product import Product

# user = User()
# user.fetch_all()
# user.fetch_one(name='harish')
# user.fetch_one(id=2)
# user.fetch_columns(('name',), lookup="id = 3")
# user.insert({'name': 'tarun', 'email': 'tarun.sahu.bpl@gmail.com'})
# user.delete(lookup="id = 3")

# user.update('id = 3', {'name': 'rakesh moni gupta', 'email': 'monirakesh@gmail.com'})
# data = user.fetch_all()
# print(data)

product = Product()
# product.insert({'title': '3 Idiots', "description": "Engineering college life", "price": 199})
data = product.fetch_columns(('title', 'price'))
print(data)

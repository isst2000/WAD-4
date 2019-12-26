from lab4.blog.models import Connection, Userr

connection = Connection("dbuser", "123", "first_db")

with connection:
    user = Userr(connection, 'Жолина', '10', 'puravleva@gmail.com')
    user.save()

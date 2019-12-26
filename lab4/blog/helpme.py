import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='dbuser',
                             password='123',
                             db='first_db',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:

        # Вставка записи
        sql_request = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
        cursor.execute(sql_request, ('Рома', '3', 'rauger474@mail.ru'))

    # Зафиксировать изменения
    connection.commit()

    with connection.cursor() as cursor:
        # Выполним выборку
        sql_request = "SELECT * FROM users"
        cursor.execute(sql_request)
        result = cursor.fetchall()

        print(result)
finally:
    connection.close()

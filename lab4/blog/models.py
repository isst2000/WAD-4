from django.db import models

import pymysql


class Post(models.Model):
    post_head = models.CharField(max_length=70)
    post_text = models.CharField(max_length=255)
    publication_date = models.DateField('Date published')

    def __str__(self):
        return self.post_head


class Comment(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=70)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.answer_text


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Userr:

    def __init__(self, db_connection, name, age, email):
        self.db_connection = db_connection.connection,
        self.name = name,
        self.age = age,
        self.email = email

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO users (name, age, email) VALUES (%s, %s, %s)", ('Настя', '3', 'rauger474@mail.ru'))
        self.db_connection.commit()
        c.close()


class UserModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=30)




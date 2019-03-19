from peewee import *

db = SqliteDatabase('social.db')

class Entry(Model):
    title = TextField()  # title is an instance of the TextField class

    class Meta:
        database = db
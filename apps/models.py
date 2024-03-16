from django.contrib.auth.models import User
from django.db.models import Model, TextField, ForeignKey, CASCADE, CharField


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=100)
    description = TextField()
    owner = ForeignKey(User, on_delete=CASCADE)

from django.db import models
from djongo import models as djongo_models

class User(djongo_models.Model):
    _id = djongo_models.ObjectIdField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'users'
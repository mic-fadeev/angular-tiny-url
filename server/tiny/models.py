from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from random import randint


class UserManager(models.Manager):
    def random(self):
        count = self.aggregate(ids=Count('id'))['ids']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class MyUser(User):
    objects = UserManager()

    class Meta:
        proxy = True

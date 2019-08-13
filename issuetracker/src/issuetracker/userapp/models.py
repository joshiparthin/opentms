from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=10)

    def __str__(self):
        return "username:" + str(self.username)



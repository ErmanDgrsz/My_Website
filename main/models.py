from django.db import models


class Account(models.Model):
    email = models.EmailField(max_length=60)

from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.IntegerField(default=1000)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    transaction_type = models.CharField(max_length=50)

    amount = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
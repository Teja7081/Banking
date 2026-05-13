from django.db import models

from django.contrib.auth.models import User


class Account(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    balance = models.IntegerField(default=1000)

    account_number = models.CharField(
        max_length=14,
        unique=True
    )

    upi_id = models.CharField(
        max_length=100,
        unique=True
    )

    card_number = models.CharField(
        max_length=16
    )

    cvv = models.CharField(
        max_length=3
    )

    expiry_date = models.CharField(
        max_length=10
    )

    ifsc_code = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.user.username


class Transaction(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    transaction_type = models.CharField(
        max_length=50
    )

    amount = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username
    
class Card(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    card_number = models.CharField(
        max_length=16
    )

    cvv = models.CharField(
        max_length=3
    )

    expiry_date = models.CharField(
        max_length=10
    )

    card_type = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.card_number
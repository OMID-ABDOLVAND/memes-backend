from django.db import models


# Create your models here.


class Account(models.Model):
    wallet_address = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" wallet: {self.wallet_address} -  email: {self.email}"

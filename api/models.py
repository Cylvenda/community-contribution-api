from django.db import models
from django.conf import settings


class Contributions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="User_create",
        on_delete=models.PROTECT,
    )
    targeted_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="targeted_user",
        on_delete=models.PROTECT,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contributors(models.Model):
    NORMAL_PAYMENT = "N"
    PHONE_PAYMENT = "P"
    BANK_PAYMENT = "B"

    PAYMENT_METHODS = [
        (NORMAL_PAYMENT, "Normal Payments"),
        (PHONE_PAYMENT, "Mobile Phone Payments"),
        (BANK_PAYMENT, "Bank Payments"),
    ]
    Contributions = models.ForeignKey(
        Contributions, related_name="contributors", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_contributed",
        on_delete=models.PROTECT,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=5, choices=PAYMENT_METHODS, default=NORMAL_PAYMENT
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount

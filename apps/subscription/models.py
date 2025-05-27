from django.db import models

class Subcription(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    plan = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    checkmark = models.CharField(max_length=100)

    def __str__(self):
        return self.plan


class Payment(models.Model):
    stripe_payment_intent = models.CharField(max_length=100)
    amount = models.IntegerField()  # Amount in cents
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.amount}"


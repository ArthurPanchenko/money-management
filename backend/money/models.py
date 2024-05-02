from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()
current_date = datetime.now().date()


class Wallet(models.Model):
    user = models.OneToOneField(user, blank=True, null=True, on_delete=models.CASCADE)
    left_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    left_date = models.DateField(default=current_date + timedelta(days=7))
    daily = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def left_days(self):
        left_days = self.left_date - current_date
        return left_days.days

    def calculate_daily(self):
        self.daily = round(self.left_money / self.left_days, 2)
        self.save()
        return self

    def decrease_money(self, amount):
        if self.left_money < amount:
            self.left_money = 0
        else:
            self.left_money -= amount
        self.save()
        

class Purchase(models.Model):
    wallet = models.ForeignKey(
        Wallet, 
        on_delete=models.CASCADE, 
        related_name='purchases'
    )
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    purchase_date = models.DateTimeField(auto_now_add=True, blank=True)
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()
current_date = datetime.now().date()


class Wallet(models.Model):
    user = models.OneToOneField(user, blank=True, null=True, on_delete=models.CASCADE)
    left_money = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    left_date = models.DateField(default=current_date + timedelta(days=7))

    @property
    def left_days(self):
        left_days = self.left_date - current_date
        return left_days.days

    @property
    def daily_available(self):
        return round(self.left_money / self.left_days, 2)

    def decrease_money(self, amount):
        if self.left_money < amount:
            self.left_money = 0
        self.save()
        


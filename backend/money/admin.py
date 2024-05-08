from django.contrib import admin

from .models import Wallet, Purchase


admin.site.register(Wallet)
admin.site.register(Purchase)
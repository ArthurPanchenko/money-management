from money_management.celery import app

from .models import Wallet


@app.task
def recalculate_daily():
    wallets = Wallet.objects.all()
    for wallet in wallets:
        wallet.calculate_daily()
from rest_framework import serializers

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):

    # user = serializers.CharField(read_only=True)
    # left_date = serializers.DateField(read_only=True)
    # left_money = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Wallet
        fields = (
            'user',
            'left_money',
            'left_date',
            'left_days',
            'daily_available',
        )



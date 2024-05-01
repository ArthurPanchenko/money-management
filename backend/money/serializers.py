from rest_framework import serializers

from .models import Wallet, Purchase


class PurchaseSerializer(serializers.ModelSerializer):

    wallet = serializers.CharField(read_only=True)

    class Meta:
        model = Purchase
        fields = (
            'wallet',
            'title',
            'amount',
        )


class WalletSerializer(serializers.ModelSerializer):

    user = serializers.CharField(read_only=True)
    purchases = PurchaseSerializer(
        many=True,
        read_only=True
    )


    class Meta:
        model = Wallet
        fields = (
            'user',
            'left_money',
            'left_date',
            'left_days',
            'daily_available',
            'purchases'
        )



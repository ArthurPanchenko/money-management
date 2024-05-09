from rest_framework import serializers

from .models import Wallet, Purchase


class PurchaseSerializer(serializers.ModelSerializer):

    purchase_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Purchase
        ordering = ['purchase_date']
        
        fields = (
            'title',
            'amount',
            'purchase_date'
        )


class WalletSerializer(serializers.ModelSerializer):

    user = serializers.CharField(read_only=True)
    daily = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    available_today = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    purchases = PurchaseSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Wallet
        fields = (
            'user',
            'left_money',
            'left_date',
            'left_days',
            'daily',
            'purchases',
            'available_today'
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance.calculate_daily()


from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    GenericAPIView
)
from rest_framework import status
from rest_framework.response import Response

from .models import Wallet, Purchase
from .serializers import WalletSerializer, PurchaseSerializer


class WalletView(RetrieveUpdateAPIView):

    serializer_class = WalletSerializer

    def get_object(self):
        return get_object_or_404(Wallet, pk=self.kwargs.get('pk'))
    

class PurchaseListView(ListCreateAPIView):
    serializer_class = PurchaseSerializer
    
    def get_queryset(self):
        return Purchase.objects.filter(wallet_id=self.kwargs.get('pk'))
    
    def perform_create(self, serializer):
        serializer.validated_data['wallet_id'] = self.kwargs.get('pk')
        serializer.save()

   
class PurchaseView(GenericAPIView):
    serializer_class = PurchaseSerializer
    
    def get_queryset(self):
        wallet = get_object_or_404(Wallet, pk=self.kwargs.get('pk'))
        return Purchase.objects.filter(wallet=wallet)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        purchase_serializer = self.get_serializer(data=request.data)
        wallet = get_object_or_404(Wallet, pk=self.kwargs.get('pk'))
        
        purchase_serializer.is_valid(raise_exception=True)
        purchase_serializer.validated_data['wallet_id'] = self.kwargs.get('pk')

        wallet.decrease_money(purchase_serializer.validated_data['amount'])
        wallet.save()
        purchase_serializer.save()
        return Response(purchase_serializer.data, status=status.HTTP_201_CREATED)

        
        

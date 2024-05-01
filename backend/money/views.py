from django.shortcuts import get_object_or_404

from rest_framework.generics import RetrieveAPIView

from .models import Wallet
from .serializers import WalletSerializer


class WalletView(RetrieveAPIView):

    serializer_class = WalletSerializer

    def get_object(self):
        return get_object_or_404(Wallet, user=self.request.user)
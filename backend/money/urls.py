from django.urls import path

from . import views  


urlpatterns = [
    path('<int:pk>/', views.WalletView.as_view()),
    path('<int:pk>/purchase/', views.PurchaseView.as_view())
]
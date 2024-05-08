from django.urls import path

from . import views  


urlpatterns = [
    path('', views.WalletView.as_view()),
    path('purchase/', views.PurchaseView.as_view()),
    path('test', views.test_api)
]
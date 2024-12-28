from django.urls import path
from .views import *

urlpatterns = [
    path('', GiftVoucherAPIview.as_view(), name='gift-voucher-api'),
    path('purchases/', PurchaseView.as_view(), name='create-purchase'),
    path('purchases/confirm/', ConfirmPaymentView.as_view(), name='confirm-payment'),
]

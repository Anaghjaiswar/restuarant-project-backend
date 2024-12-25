from django.urls import path
from .views import *

urlpatterns = [
    path('', GiftVoucherAPIview.as_view(), name='gift-voucher-api'),
        
]

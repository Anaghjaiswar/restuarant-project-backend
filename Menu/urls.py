from django.urls import path
from .views import *

urlpatterns = [
    path('', MenuList.as_view()),
    path('<int:menu_id>/dishes/', DishList.as_view()),
    path('dishes/<int:dish_id>/', DishDetail.as_view()),
    path('orders/', PlaceOrderView.as_view(), name='place-order'),
    path('orders/confirm/',ConfirmPaymentView.as_view()),
]
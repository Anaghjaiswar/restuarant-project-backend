from django.urls import path
from .views import BookTableAPIview

urlpatterns = [
    path('', BookTableAPIview.as_view(), name='book-table'),
]


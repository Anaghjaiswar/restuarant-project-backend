from django.urls import path
from .views import *

urlpatterns = [
    path('',ContactAPIview.as_view(), name='contact-api'),
]

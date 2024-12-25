from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/menu/', include('Menu.urls')),
    path('api/contact/', include('Contact.urls')),
    path('api/gift-vouchers/', include('GiftVouchers.urls')),
    path('api/book-table/', include('BookTable.urls')),
]

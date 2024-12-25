from django.db import models
from cloudinary.models import CloudinaryField

class GiftVoucher(models.Model):
    title=models.CharField(max_length=100, verbose_name='Title')
    description=models.TextField(verbose_name='Description')
    price=models.FloatField(verbose_name='Price')
    image=CloudinaryField('image', null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Gift Voucher'
        verbose_name_plural='Gift Vouchers'

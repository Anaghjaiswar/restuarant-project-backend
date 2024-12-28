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


class Purchase(models.Model):
    voucher = models.ForeignKey(GiftVoucher, on_delete=models.CASCADE, related_name='purchases')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    order_id = models.CharField(max_length=100, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase of {self.voucher.title} by {self.customer_name}"

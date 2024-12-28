from rest_framework import serializers
from .models import GiftVoucher, Purchase

class GiftVoucherSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = GiftVoucher
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
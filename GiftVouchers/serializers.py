from rest_framework import serializers
from .models import GiftVoucher

class GiftVoucherSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    
    class Meta:
        model = GiftVoucher
        fields = '__all__'

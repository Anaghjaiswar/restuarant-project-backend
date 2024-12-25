from rest_framework import serializers
from .models import BookTable

class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = ['id', 'first_name', 'last_name', 'number', 'email', 'date', 'start_time', 'end_time', 'guests', 'message', 'created_at']
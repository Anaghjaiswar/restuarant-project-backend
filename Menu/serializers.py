from rest_framework import serializers
from .models import Menu, Dish, Order, OrderItem

class DishSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='menu.category_name', read_only=True)
    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'price', 'category_name']

class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'


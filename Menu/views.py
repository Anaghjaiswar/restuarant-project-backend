from django.shortcuts import render
from .models import Menu, Dish
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MenuSerializer, DishSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class MenuList(APIView):
    def get(self, request):
        try:
            menus = Menu.objects.all()
            serializer = MenuSerializer(menus, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)})  
        
class DishList(APIView):
    def get(self, request, menu_id):
            get_object_or_404(Menu, id=menu_id)
            dishes=Dish.objects.filter(menu=menu_id)
            serializer=DishSerializer(dishes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class DishDetail(APIView):
    def get(self,request,dish_id):
        try:
            dish=Dish.objects.get(id=dish_id)
            serializer=DishSerializer(dish)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)})            

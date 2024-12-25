from django.shortcuts import render
from rest_framework import viewsets
from .models import GiftVoucher
from .serializers import GiftVoucherSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class GiftVoucherAPIview(APIView):
    def get(self, request):
        try:
            gift_vouchers = GiftVoucher.objects.all()
            serializer = GiftVoucherSerializer(gift_vouchers, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)})

    def post(self, request):
        try:
            serializer = GiftVoucherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)})
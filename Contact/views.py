from django.shortcuts import render
from .models import Contact
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContactSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail



class ContactAPIview(APIView):
    """
    Handle Contact Form Submission
    """

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            user_email = serializer.data['email']
            user_name = serializer.data['name']

            send_mail(
                subject="Thank You for Contacting Us",
                message=f"Dear {user_name},\n\nThank you for reaching out. We have received your message and will get back to you soon.\n\nRegards,\nRestaurant Team",
                from_email="jaiswaranagh@gmail.com",
                recipient_list=[user_email],
                fail_silently=False,
            )
            return Response({"message":"Contact Form Submitted Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
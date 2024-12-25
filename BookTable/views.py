from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BookTable
from .serializers import BookTableSerializer
from django.core.mail import send_mail

# Create your views here
class BookTableAPIview(APIView):
    """
    Handle Book Table API
    """

    def post(self,request, *args, **kwargs):
        serializer = BookTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer. save()

            user_email = serializer.data['email']
            user_fname = serializer.data['first_name']
            user_lname = serializer.data['last_name']
            user_date = serializer.data['date']
            user_guests = serializer.data['guests']
            user_number = serializer.data['number'] 
            user_start_time = serializer.data['start_time']
            user_end_time = serializer.data['end_time']
            user_message = serializer.data['message']

            send_mail(
                subject="table booking details",
                message=f"""Dear {user_fname} {user_lname},
                Thank you for booking a table with us.
                here are your booking details: 
                Date: {user_date}
                Guests: {user_guests}
                Number: {user_number}
                Start Time: {user_start_time}
                End Time: {user_end_time}
                Message: {user_message}

                We will soon get back to you with the confirmation details. Thank you for choosing us.

                Regards,
                LazeezEats Team""",
                from_email="jaiswaranagh@gmail.com",
                recipient_list=[user_email],
                fail_silently=False,
            )
            return Response({"message":"book Table form submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from .models import Menu, Dish, Order, OrderItem
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MenuSerializer, DishSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from .utils.razorpay_client import client
import razorpay
from django.core.mail import send_mail
from django.conf import settings


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

class PlaceOrderView(APIView):
    def post(self, request):
        data = request.data
        try:
            # Create an order
            order = Order.objects.create(contact_number=data['contact_number'],email=data['email'])

            
            # Add items to the order
            total_amount = 0
            for item in data['order_items']:
                menu = Menu.objects.get(id=item['menu_id'])
                dish = Dish.objects.get(id=item['dish_id'])
                total_amount += dish.price * item['quantity']

                OrderItem.objects.create(
                    order=order,
                    menu=menu,
                    dish=dish,
                    quantity=item['quantity'],
                    special_requests=item.get('special_requests', '')
                )

            razorpay_order = client.order.create({
                "amount": int(total_amount * 100),  # Amount in paise
                "currency": "INR",
                "receipt": f"order_{order.id}",
            })
            order.razorpay_order_id = razorpay_order['id']
            order.save()

            return Response({
                "message": "Order placed successfully",
                "order_id": order.id,
                "razorpay_order_id": razorpay_order['id'],
                "amount": total_amount
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class ConfirmPaymentView(APIView):
    def post(self, request):
        data = request.data
        try:
            razorpay_order_id = data.get('razorpay_order_id')
            razorpay_payment_id = data.get('razorpay_payment_id')

            if not razorpay_order_id or not razorpay_payment_id:
                return Response({"error": "Missing razorpay_order_id or razorpay_payment_id"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Fetch the order
            order = Order.objects.get(razorpay_order_id=razorpay_order_id)

            # Verify the payment signature (optional)
            # params_dict = {
            #     'razorpay_order_id': razorpay_order_id,
            #     'razorpay_payment_id': razorpay_payment_id,
            # }
            try:
                client.payment.fetch(razorpay_payment_id)
            except razorpay.errors.BadRequestError:
                return Response({"error": "Invalid payment ID"}, status=status.HTTP_400_BAD_REQUEST)

            # Mark the order as paid
            order.razorpay_payment_id = razorpay_payment_id
            order.is_paid = True
            order.save()

            # Send email notification
            subject = f"Order Confirmation - Order #{order.id}"
            message = f"""
            Dear Customer,
            
            Thank you for your order!
            
            Your order #{order.id} has been successfully placed and confirmed. 
            Order details:
            
            Items:
            """
            # Add ordered items to the email message
            for item in order.order_items.all():
                message += f"- {item.quantity} x {item.dish.name} ({item.menu.category_name}) - ₹{item.dish.price}\n"

            message += f"\nTotal Amount Paid: ₹{sum(item.dish.price * item.quantity for item in order.order_items.all())}\n\n"
            message += "We hope you enjoy your meal!\n\nBest regards,\nLazzez-Eats Team"

            recipient_email = order.email

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient_email],
                fail_silently=False,
            )

            return Response({"message": "Payment confirmed successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

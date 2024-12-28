from django.shortcuts import render
from rest_framework import viewsets
from .models import GiftVoucher, Purchase
from .serializers import GiftVoucherSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .utils.razorpay_client import client
import razorpay
from django.core.mail import send_mail
from django.conf import settings

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
        

class PurchaseView(APIView):
    def post(self, request):
        try:
            voucher_id= request.data.get('voucher_id')
            customer_name=request.data.get('customer_name')
            customer_email=request.data.get('customer_email')

            voucher = GiftVoucher.objects.get(id=voucher_id)

            amount = int(voucher.price * 100)
            razorpay_order = client.order.create({
                "amount": amount,
                "currency": "INR",
                "payment_capture" : "1"
            })

            purchase = Purchase.objects.create(
                voucher=voucher,
                customer_name=customer_name,
                customer_email=customer_email,
                order_id=razorpay_order['id'],
                paid=False
            )

            return Response({
                "order_id": razorpay_order['id'],
                "amount": voucher.price,
                "currency": "INR"
            }, status=status.HTTP_201_CREATED)
        
        except GiftVoucher.DoesNotExist:
            return Response({"error":"Voucher not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ConfirmPaymentView(APIView):
    def post(self, request):
        try:
            order_id = request.data.get('order_id')
            razorpay_payment_id = request.data.get('razorpay_payment_id')
            voucher_id = request.data.get('voucher_id')

            # Verify payment using Razorpay's SDK (optional)
            try:
                client.payment.fetch(razorpay_payment_id)
            except razorpay.errors.BadRequestError:
                return Response({"error": "Invalid payment ID"}, status=status.HTTP_400_BAD_REQUEST)

            # Update Purchase entry
            purchase = Purchase.objects.get(order_id=order_id, voucher_id=voucher_id)
            purchase.razorpay_payment_id = razorpay_payment_id
            purchase.paid = True
            purchase.save()

            subject = "Payment Confirmation - Gift Voucher"
            message = f"""
            Dear {purchase.customer_name},

            Thank you for your purchase of the gift voucher: {purchase.voucher.title}.
            
            Payment Details:
            - Amount Paid: ₹{purchase.voucher.price}
            - Payment ID: {razorpay_payment_id}

            Your order has been successfully processed.

            Best regards,
            The Restaurant Team
            """

            recipient_email = purchase.customer_email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient_email],
                fail_silently=False,
            )

            return Response({"success": True, "message": "Payment confirmed!"}, status=status.HTTP_200_OK)

        except Purchase.DoesNotExist:
            return Response({"error": "Purchase not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      



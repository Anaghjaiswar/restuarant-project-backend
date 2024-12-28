from django.db import models

class Menu(models.Model):
    """
    Represents a menu category (e.g., Veg Menu, Non-Veg Menu, etc.)
    """
    CATEGORY_CHOICES = [
        ('veg', 'Veg Menu'),
        ('non_veg', 'Non-Veg Menu'),
        ('dessert', 'Desserts Menu'),
        ('beverage', 'Beverages Menu')
    ]

    category_name = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        unique=True,
        verbose_name="Menu Category"
    )
    
    def __str__(self):
        return self.get_category_name_display()

class Dish(models.Model):
    """
    Represents a dish within a specific menu.
    """
    menu = models.ForeignKey(Menu, related_name="dishes", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Dish Name")
    description = models.TextField(verbose_name="Dish Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price (₹)")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Order(models.Model):
    """
    Represents an order placed by a user.
    """
    contact_number = models.CharField(max_length=15, verbose_name="Contact Number")
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    razorpay_order_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="Razorpay Order ID")
    razorpay_payment_id = models.CharField(max_length=255, null=True, blank=True, verbose_name="Razorpay Payment ID")
    is_paid = models.BooleanField(default=False, verbose_name="Is Paid")

    def __str__(self):
        return f"Order #{self.id} - {self.contact_number}"


class OrderItem(models.Model):
    """
    Represents a specific item in an order.
    """
    order = models.ForeignKey(Order, related_name="order_items", on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name="Menu")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Dish")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    special_requests = models.TextField(null=True, blank=True, verbose_name="Special Requests")

    def __str__(self):
        return f"{self.quantity}x {self.dish.name} in Order #{self.order.id}"


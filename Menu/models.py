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

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    """
    Represents a contact form submission.
    """
    name = models.CharField(max_length=100, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Mobile number must be exactly 10 digits.",
                code='invalid_mobile_number'
            )
        ],
        verbose_name="Mobile Number"
    )
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
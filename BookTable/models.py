from django.db import models
from django.core.validators import RegexValidator
import datetime
from django.core.exceptions import ValidationError

class BookTable(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
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
    email = models.EmailField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    guests = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    
    def validate_date(self):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past.")
        
    def validate_time(self):
        if self.start_time > self.end_time:
            raise ValidationError("The start time cannot be after the end time.")
        
    def clean(self):
        self.validate_date()
        self.validate_time()

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Book Table"
        verbose_name_plural = "Book Tables"
        
    
    

from django.db import models

# Class for Turf model 
class TurfDB(models.Model): 
    turf_name = models.CharField(max_length=100) 
    location = models.CharField(max_length=200) 
    surface_type = models.CharField(max_length=50) 
    price_per_hour = models.PositiveIntegerField() 
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.turf_name

# Class for Booking model 
class BookingDB(models.Model): 
    customer_name = models.CharField(max_length=100) 
    phone = models.CharField(max_length=15) 
    turf_id = models.IntegerField() 
    booking_date = models.DateField() 
    start_time = models.TimeField() 
    duration_hours = models.PositiveIntegerField(default=1) 
    total_amount = models.PositiveIntegerField(editable=False, null=True) 
    status = models.CharField(max_length=50, default='Pending') 
    created_at = models.DateTimeField(auto_now_add=True)




# Create your models here.

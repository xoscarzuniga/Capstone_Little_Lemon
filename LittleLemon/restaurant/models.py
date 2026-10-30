from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateTimeField(auto_now=True, auto_now_add=False)

class Menu(models.Model):
    title = models.CharField( max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    

from django.db import models
#importing djnago built-in user to handle user authentication and authorization.
from django.contrib.auth.models import User

# Create your models here.
class Receipt (models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=25)
    date_of_purchase = models.DateField()
    item_list = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places= 2)

    def __str__(self):
# String representation of a Receipt instance for better readability (the  receipt is saved and known by its name- date of pur)
        return f"{self.store_name} - {self.date_of_purchase}"
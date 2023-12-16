from django import forms
from .models import Receipt



# Define a form named 'ReceiptForm' based on the model 'Receipt'
class ReceiptForm(forms.ModelForm):
    class Meta:

        # Specify the model associated with the form
        model = Receipt
        # Define the fields to include in the form
        fields = ['store_name', 'date_of_purchase', 'item_list', 'total_amount']

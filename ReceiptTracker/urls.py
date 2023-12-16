from django.urls import path
from .views import CustomRegisterView, CustomLoginView, CustomLogoutView, ReceiptListView, ReceiptDetailView, ReceiptFormView

# Define URL patterns for the application
urlpatterns = [
  
    path('signup/', CustomRegisterView.as_view(), name='signup'),  # URL pattern for user registration view
    path('login/', CustomLoginView.as_view(), name='custom_login'), # URL pattern for user login view
    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),# URL pattern for user logout view

    path('receipt_list/', ReceiptListView.as_view(), name='receipt_list'), # URL pattern for displaying a list of receipts
    path('receipt_detail/<int:receipt_id>/', ReceiptDetailView.as_view(), name='receipt_detail'),# URL pattern for displaying details of a specific receipt
    path('receipt_form/add/', ReceiptFormView.as_view(), name='receipt_form'),    # URL pattern for adding or editing a receipt
]
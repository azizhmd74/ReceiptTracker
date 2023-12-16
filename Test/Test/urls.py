from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Test/', include('ReceiptTracker.urls')),# the path to our main application 
]

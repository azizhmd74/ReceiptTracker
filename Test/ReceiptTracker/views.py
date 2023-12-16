from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.views.generic import ListView
from .models import Receipt
from .forms import ReceiptForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

class CustomLoginView(View):
    template_name = 'registration/login.html'

    def get(self, request):
        # Display login form for GET requests
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Process login form for POST requests
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('receipt_list')
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, self.template_name, {'form': form})



class CustomLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        # Logout user for GET requests
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('custom_login')

    def post(self, request):
        # Handle POST requests if needed
        # For example, you might want to log the user out even for POST requests
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('custom_login')
    
    
class CustomRegisterView(View):
    template_name = 'registration/signup.html'

    def get(self, request):
        # Display registration form for GET requests
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Process registration form for POST requests
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('receipt_list')
        return render(request, self.template_name, {'form': form})


class ReceiptListView(LoginRequiredMixin, ListView):
    template_name = 'receipts/receipt_list.html'
    context_object_name = 'receipts'

    def get_queryset(self):
        # Filter receipts based on the current user
        return Receipt.objects.filter(user=self.request.user)
    

class ReceiptDetailView(LoginRequiredMixin, View):
    template_name = 'receipts/receipt_detail.html'
    context_object_name = 'receipt'
    pk_url_kwarg = 'receipt_id'  # Use the correct keyword argument

    def get(self, request, receipt_id):
        # Retrieve the receipt for the authenticated user
        receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
        form = ReceiptForm(instance=receipt)
        return render(request, self.template_name, {'receipt': receipt, 'form': form})

    def post(self, request, receipt_id):
        # Retrieve the receipt for the authenticated user
        receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
        
        # Process form submission for editing
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            form.save()
            messages.success(request, 'Receipt updated successfully.')
            return redirect('receipt_detail', receipt_id=receipt.id)
        
        # If the form is not valid, render the detail view with the form to display validation errors
        return render(request, self.template_name, {'receipt': receipt, 'form': form})
    


@method_decorator(login_required, name='dispatch')
class ReceiptFormView(View):
    # Template file for rendering the form
    template_name = 'receipts/receipt_form.html'

    def get(self, request, receipt_id=None):
        # Retrieve an existing receipt if receipt_id is provided, otherwise create a new one
        if receipt_id:
            receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
        else:
            receipt = Receipt(user=request.user)

        # Create a form instance based on the receipt
        form = ReceiptForm(instance=receipt)

        # Render the template with the form
        return render(request, self.template_name, {'form': form})

    def post(self, request, receipt_id=None):
        # Retrieve an existing receipt if receipt_id is provided, otherwise create a new one
        if receipt_id:
            receipt = get_object_or_404(Receipt, id=receipt_id, user=request.user)
        else:
            receipt = Receipt(user=request.user)

        # Create a form instance based on the form data and the receipt
        form = ReceiptForm(request.POST, instance=receipt)

        # If the form is valid, save the form data and redirect to the receipt list view
        if form.is_valid():
            form.save()
            return redirect('receipt_list')

        # If the form is not valid, render the template with the form to display validation errors
        return render(request, self.template_name, {'form': form})
    

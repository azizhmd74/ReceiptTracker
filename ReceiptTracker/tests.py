
from msilib.schema import SelfReg
import pdb
from typing import Self  # For interactive debugging
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from requests import Response
from .models import Receipt

class ReceiptModelAndViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_receipt(self):
        # Model test
        receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item_list='Item1, Item2',
            total_amount=100.50
        )
        self.assertEqual(receipt.store_name, 'Test Store')
        self.assertEqual(receipt.user, self.user)
        # Add more assertions based on your model fields

    def test_receipt_list_view(self):
        # View test
        response = self.client.get(reverse('receipt_list'))
        self.assertEqual(response.status_code, 200)
        
        # Check if 'receipts/receipt_list.html' is used without checking 'base.html'
        self.assertTemplateUsed(response, 'receipts/receipt_list.html')

def test_receipt_detail_view(self):
        # View test
        receipt = Receipt.objects.create(
            user=self.user,
            store_name='Test Store',
            date_of_purchase='2023-01-01',
            item_list='Item1, Item2',
            total_amount=100.50
        )

        response = self.client.get(reverse('receipt_detail', args=[receipt.id]))
        self.assertEqual(response.status_code, 200)

        # Debugging: Print templates used
        print(response.templates)

        self.assertTemplateUsed(response, 'receipts/receipt_detail.html')  # Check the correct path

def test_receipt_form_view(self):
        # View test
        response = self.client.get(reverse('receipt_form'))
        self.assertEqual(response.status_code, 200)

        # Debugging: Print templates used
        print(response.templates)

        self.assertTemplateUsed(response, 'receipts/receipt_form.html')  # Check the correct path
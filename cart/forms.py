from django import forms
from cart.models import Order,OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['fullName','address','city','phone']
        
class OrderItemForm(forms.ModelForm):
    class Meta:
        model: OrderItem
        fields = [None]
from django import forms
from store.models import BidProduct, StockProduct

class BidForm(forms.ModelForm):
    currentBid = forms.IntegerField(label="Tu Puja")
    class Meta:
        model = BidProduct
        fields = ['currentBid']
        
class BidProductForm(forms.ModelForm):
    class Meta:
        model = BidProduct
        #fields = '__all__'
        exclude = ['seller', 'bidWinner', 'currentBid','sold']
    
class StockProductForm(forms.ModelForm):
    class Meta:
        model = StockProduct
        exclude = ['seller','sold']

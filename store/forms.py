from django import forms
from store.models import BidProduct, StockProduct

class BidForm(forms.ModelForm):
    currentBid = forms.IntegerField(widget=forms.NumberInput(None))
    class Meta:
        model = BidProduct
        fields = ['currentBid']
        
class BidProductForm(forms.ModelForm):
    class Meta:
        model = BidProduct
        #fields = '__all__'
        exclude = ['seller', 'bidWinner', 'currentBid']
    
class StockProductForm(forms.ModelForm):
    class meta:
        model = StockProduct
        exclude = ['seller']

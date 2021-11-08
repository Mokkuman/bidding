from django import forms
from store.models import BidProduct

class BidForm(forms.ModelForm):
    currentBid = forms.IntegerField(widget=forms.NumberInput(None))
    class Meta:
        model = BidProduct
        fields = ['currentBid']
from django.contrib import admin
#from store.models import User
from .models import User, Bid
from store.models import BidProduct, StockProduct
# Register your models here.
#admin.site.register(User)
admin.site.register(User)
admin.site.register(Bid)
admin.site.register(BidProduct)
admin.site.register(StockProduct)
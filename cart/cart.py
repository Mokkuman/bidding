from store.models import StockProduct
from decimal import Decimal

class Cart():
    #Manejo de cookies
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('skey')#Session key
        #Si el usuario no tiene datos guardados en sus cookies
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}#Carrito empieza vacío
        self.cart = cart
        
    def add(self,product):
        product_id = str(product.id)
        #Primero verificar si hay suficiente stock
        if product_id in self.cart:
            self.cart[product_id]['qty']+=1
        else:
            self.cart[product_id]={'price':str(product.price),'qty':1}
            
        self.save()
        
    #Regresa el numero total de productos añadidos al carrito
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

 
    #Funcion iterable para recolectar los valores de la base de datos
    def __iter__(self):
        product_ids = self.cart.keys()
        products = StockProduct.products.filter(id__in=product_ids)
        cart = self.cart.copy()
        #Almacena los productos
        for product in products:
            cart[str(product.id)]['product'] = product
        #Calcula el precio
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['qty']
            yield item
    
    def getProducts(self):
        products_ids = self.cart.keys()
        products = StockProduct.products.filter(id__in=products_ids)
        products(type(products))
        return products
    
    def get_price(self,product_id):
        return (int(self.cart[product_id]['qty']))*(float(self.cart[product_id]['price']))
    
    def get_qty(self,product_id):
        return int(self.cart[product_id]['qty'])
    
    def get_total_price(self):
        return sum(((float(item['price']))*(int(item['qty'])) for item in self.cart.values()))
    
    def delete(self,product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()
        
    def deleteAll(self):
        self.cart.clear()
        self.save()
            
    #Guarda los cambios realizados
    def save(self):
        self.session.modified = True
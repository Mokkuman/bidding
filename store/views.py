from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def productListing(request):
    return HttpResponse("Products:")

def categories(request):
    return HttpResponse("Categories: ") #Solo es un ejemplo

def goToProduct(request):
    try:
        dummyData = {
            'name':'Product 1XX',
            'currentBid':100,
            'description':'Very cool treasure box',
            'category':'TOYS',
            'condition':'LIKE NEW'
        }
        return render(request, 'store/productTemplate.html',{
            'product':dummyData,
            'productFound':True
        })
    except Exception as exception:
        return render(request, "store/productTemplate.html",{
            'productFound':False
        })

def FAQ(request):
     return HttpResponse("""<div><h3><FONT SIZE=20 COLOR=#ef476f>Preguntas Frecuentes</h3></FONT>
     <div><FONT SIZE=6 COLOR=#073b4c>¿Cómo agrego artículos a mi carrito?</FONT>
      <FONT SIZE=4><p>Una vex hayas iniciado sesión, da clic en cualquier artículo que desees obtener y 
      luego da clic en Agregar al carrito. ¡Asi de sencillo!
      Para ver los artículos que posees en tu carrito, da clic al ícono de la parte superior.</FONT></br></p>
      <div><FONT SIZE=6 COLOR=#073b4c>¿Cómo puedo vender mis productos?</FONT>
      <FONT SIZE=4><p>Haz clic en el apartado "Mi perfil" y busca la opción "Subir un producto".
      Puedes elegir entre subir un producto con precio fijo o iniciar una puja.</FONT></br></p>
      <div><FONT SIZE=6 COLOR=#073b4c>¿Qué es una puja?</FONT>
      <FONT SIZE=4><p>Es muy similar a como funcionan las subastas. Al optar por subir tu producto
      por una puja, los demás usuarios tendrán hasta 24 horas para ofertar el mejor precio para tu 
      producto. Al finalizar el día, el usuario con la mejor propuesta económica se habrá llevado tu producto!</FONT></br></p>
      </div>""")

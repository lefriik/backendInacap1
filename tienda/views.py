from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {
        'title': 'Inicio'
    })


def pedido(request):

    productos = [
        {'name': 'JUAN VALDEZ VOLCAN', 'precio': 10000, 'descripcion':'Café de sabor profundo'}, 
        {'name': 'BIFTU GUDINA ETIOPIA', 'precio': 15000, 'descripcion':' Ejemplo de calidad'},
        {'name': 'LUCCAFE GOLD EDITION', 'precio': 30000, 'descripcion':'Cafeína extra'}
        
        ]


    return render(request, 'pedido.html', {
        'title': 'Menu' ,
        'productos': productos
    })


def blog(request):
    return render(request, 'blog.html',{
        'title': 'Blog'
    })
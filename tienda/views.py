from django.shortcuts import render

# Create your views here.


def index(request):

    imagen = '../images/header_family.webp'


    return render(request, './inicio/index.html', {
        'title': 'Inicio',
        'imagen' : imagen
    })


def productos(request):

    productos = [
        {'name': 'JUAN VALDEZ VOLCAN', 'precio': 10000, 'descripcion':'Café de sabor profundo', 'imagen': '/static/images/cafe1.webp'}, 
        {'name': 'BIFTU GUDINA ETIOPIA', 'precio': 15000, 'descripcion':' Ejemplo de calidad', 'imagen': '/static/images/cafe2.webp'},
        {'name': 'LUCCAFE GOLD EDITION', 'precio': 30000, 'descripcion':'Cafeína extra', 'imagen': '/static/images/cafe3.webp'},
        {'name': 'MARLEY COFFEE', 'precio': 25000, 'descripcion':'One Love, One Heart', 'imagen': '/static/images/cafe4.webp'},
        {'name': 'NESCAFÉ', 'precio': 18000, 'descripcion':'Fina Seleccion', 'imagen': '/static/images/cafe5.webp'},
        {'name': 'Cruzeiro', 'precio': 22000, 'descripcion':'Tostado y Molido', 'imagen': '/static/images/cafe6.webp'}
        
        ]


    return render(request, './productos/productos.html', {
        'title': 'Menu' ,
        'productos': productos,
        
    })


def blog(request):
    return render(request, './blog/blog.html',{
        'title': 'Blog'
    })


def contacto(request):
    return render(request, './contacto/contacto.html',{
        'title': 'Contacto'
    })

def siguenos(request):
    return render(request, './siguenos/siguenos.html',{
        'title': 'Siguenos'
    })

def espresso(request):
    return render(request, './promos/espresso.html',{
        'title': 'Espresso'
    })

def mocaccino(request):
    return render(request, './promos/mocaccino.html',{
        'title': 'Mocaccino'
    })
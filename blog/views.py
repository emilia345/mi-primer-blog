from django.shortcuts import render
from django.utils import timezone
from .models import paises

def lista_paises(request):
    posts = (
        paises.objects
        .filter(fecha_publicacion__lte=timezone.now()) 
        .order_by('-fecha_publicacion')                
    )
    return render(request, 'blog/lista_paises.html', {'paises': posts})
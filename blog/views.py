from django.shortcuts import render
from django.utils import timezone
from .models import paises
from .models import Publicacion

from django.contrib.auth.models import User
# Create your views here.
def lista_public(request):
    publicaciones=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    usr_id=request.GET.get('usuario')
    
    return render(request, 'blog/lista_public.html', {
        'publicaciones':publicaciones})

def lista_paises(request):
    PAISES=paises.objects.all()    
    
    return render(request, 'blog/lista_paises.html',
    {'paises':PAISES})
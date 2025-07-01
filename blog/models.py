from django.conf import settings
from django.db import models
from django.utils import timezone

class paises(models.Model):
    
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    introduccion = models.TextField()
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
def __str__(self):
    return self.titulo

from django.contrib import admin

# Register your models here.

from .models import Genero,Libro,Autor,Idioma

admin.site.register(Genero)
admin.site.register(Idioma)
admin.site.register(Autor)
admin.site.register(Libro)



from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100,
                              help_text="Nombre del autor")
    apellido_1 = models.CharField(max_length=100,
                                  help_text="Apellido (el primero si hay más de uno)")
    apellido_2 = models.CharField(max_length=100,
                                  help_text="Segundo apellido (si procede)",
                                  null=True,
                                  blank=True)
    nacimiento = models.DateField(verbose_name="Fecha de nacimiento", blank=True)
    defuncion = models.DateField(verbose_name="Fecha de fallecimiento", null=True, blank=True)
    libros = models.ManyToManyField('Libro')
    # Función de conversión a cadena del objeto
    def __str__(self):
        if self.apellido_2 in (None, ''):
            return '%s, %s' % (self.apellido_1, self.nombre)
        else:
            return '%s y %s, %s' % (self.apellido_1, self.apellido_2, self.nombre)

class Libro(models.Model):
    titulo = models.CharField(max_length=200,
                              help_text="Titulo del libro",)
    sinopsis = models.TextField(verbose_name="Sinopis del libro",
                                blank=True,
                                help_text="Breve resumen del argumento")
    isbn = models.UUIDField(max_length=13)
    autores = models.ManyToManyField('Autor',  blank=True)
    idioma = models.ForeignKey('Idioma', on_delete=models.SET_NULL, null=True, blank=True)
    genero = models.ForeignKey('Genero', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Idioma(models.Model):

    idioma = models.CharField(max_length=50, help_text="Introduce un nombre de idioma")
    codigo = models.CharField(max_length=2,
                              help_text="Introduce un código de idioma (ISO 639-1)",
                              primary_key=True)

    def __str__(self):
        return self.idioma

class Genero(models.Model):

    genero = models.CharField(max_length=50,
                              help_text="Introduce un nombre de genero (Poesia, Ciencia Ficcion, Ensayo, ...")

    def __str__(self):
        return self.genero
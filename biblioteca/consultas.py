from biblioteca.models import *
from datetime import date

print("\nLista de Idiomas")
for idioma in Idioma.objects.all():
    print("\t", idioma)

autor = Autor(nombre="Isaac")
autor.apellido_1 = "Asimov"
autor.nacimiento = date(1900,1,1)

autor.save()

for a in Autor.objects.all():
    print("\t", a)

for a in Autor.objects.order_by('apellido_1')[0:3]:
    print("\t", a)

libro1 = Libro(titulo="La fundación",
               sinopsis="Era una vez que se era",
               genero=Genero.objects.get(genero="Fantasia"),
               idioma=Idioma.objects.get(codigo="es"),
               isbn="1234567890123")

libro1.save()
libro1.autores.add(Autor.objects.get(apellido_1="Asimov"))
libro1.save()

Autor.objects.get(apellido_1="Asimov").libros.add(libro1)

libro2 = Libro(titulo="Fundación e Imperio",
               sinopsis="Era una vez que se era",
               genero=Genero.objects.get(genero="Fantasia"),
               idioma=Idioma.objects.get(codigo="es"),
               isbn="12345677890123")

libro2.save()
libro2.autores.add(Autor.objects.get(apellido_1="Asimov"))


Autor.objects.get(apellido_1="Asimov").libros.add(libro2)

libro3 = Libro(titulo="Harry Potter: la piedra filosofal",
               sinopsis="Era una vez que se era",
               isbn="12345677890321")

libro3.save()
libro3.genero=Genero.objects.get(genero="Fantasia")
libro3.idioma=Idioma.objects.get(codigo="en")
libro3.save()
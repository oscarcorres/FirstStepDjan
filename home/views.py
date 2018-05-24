from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Primer ejemplo de DJANGO</h1><b>"+
                        "<h3>Esta es la página de Inicio (Índice)</h3><b>"+
                        "<p>(Notes for building from source: <p>1) Don't do this on a standard Ubuntu installation, "
                        "as you'll probably get a ""header and source version mismatch"" error, due to conflict"
                        " between an already installed version and the newly installed one.</p> <p>2) If the make command "
                        "seems to expect further input, just be patient, as the source can take a while to compile).</p></p>")

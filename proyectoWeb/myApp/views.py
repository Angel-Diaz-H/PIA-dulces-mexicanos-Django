from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def pagina_principal(request):
    return render(request, 'myApp/index.html')
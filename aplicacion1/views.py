from django.shortcuts import render

def vista_inicio(request):
    return render(request, 'aplicacion1/inicio.html')

def vista_servicios(request):
    return render(request, 'aplicacion1/Vista2.html')
from django.shortcuts import render

def vista_inicio(request):
    return render(request, 'aplicacion2/inicio.html')

def vista_servicios(request):
    return render(request, 'aplicacion2/Vista2.html')
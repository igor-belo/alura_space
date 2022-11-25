from django.shortcuts import render


def index(request):
    return render(request, 'galeria/index.html')

def carinanebula(request):
    return render(request, 'galeria/carinanebula.html')

def smacs(request):
    return render(request, 'galeria/smacs.html')

def stephan(request):
    return render(request, 'galeria/stephan.html')
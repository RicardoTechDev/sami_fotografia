from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
        context = {
                }
        return render(request, 'index.html', context)


def nosotros(request):
        return redirect(f'http://127.0.0.1:8000/#nosotros')


def galeria(request):
        return redirect(f'http://127.0.0.1:8000/#galeria')


def testimonios(request):
        return redirect(f'http://127.0.0.1:8000/#testimonios')


def packages(request):
        context = {
        }
        return render(request, 'packages.html', context)


def photobooth_360(request):
        context = {
        }
        return render(request, 'photobooth_360.html', context)

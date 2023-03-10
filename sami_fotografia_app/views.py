from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
        context = {
                }
        return render(request, 'index.html', context)


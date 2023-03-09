from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('galeria', views.galeria, name='galeria'),
    path('testimonios', views.testimonios, name='testimonios'),
    path('packages', views.packages, name='packages'),
]
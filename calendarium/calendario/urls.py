from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('vistamensual',views.vistamensual,name='vistamensual'),
    path('vistatrackers',views.vistatrackers,name='vistatrackers'),
    path('ayuda',views.ayuda,name='ayuda'),
    path('error404',views.error404,name='error404'),
]
from django.urls import path
from . import views
from .views import RegistroView

urlpatterns = [
    path('',views.vistasignup,name='vistasignup'),
    path('signup2',RegistroView.as_view(),name='RegistroView'),
    path('login',views.login,name='login'),
    path('logout',views.CustomLogoutView.as_view(),name='logout'),
]
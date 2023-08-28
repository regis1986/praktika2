from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('komandos/', views.komandos, name='visos-komandos')
    ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('komandos/', views.komandos, name='visos-komandos'),
    path('komandos/<int:komanda_id>', views.komanda1, name='viena-komanda'),
    ]

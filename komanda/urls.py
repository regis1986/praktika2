from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('komandos/', views.komandos, name='visos-komandos'),
    path('komandos/<int:komanda_id>', views.komanda1, name='viena-komanda'),
    path('zaidejai/', views.ZaidejasListView.as_view(), name='visi-zaidejai'),
    path('zaidejai/<int:pk>', views.ZaidejasDetailView.as_view(), name='vienas-zaidejas'),
    path('paieska/', views.search, name='paieska-url'),
    ]

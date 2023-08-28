from django.shortcuts import render, get_object_or_404
from .models import Komanda, Zaidejas
from django.views import generic
from django.db.models import Q
# from django.http import HttpResponse

def index(request):
    num_komandos = Komanda.objects.all().count()
    num_zaidejai = Zaidejas.objects.count()

    context_t = {
        'num_komandos_t': num_komandos,
        'num_zaidejai_t': num_zaidejai,
    }

    return render(request, 'index.html', context=context_t)


def komandos(request):
    visos_komandos = Komanda.objects.all()
    # print(authors)
    context_t = {
        'visos_komandos_t': visos_komandos
    }
    return render(request, 'visos_komandos.html', context=context_t)


def komanda1(request, komanda_id):
    viena_komanda = get_object_or_404(Komanda, pk=komanda_id)
    context_t = {
        'viena_komanda_t': viena_komanda
    }
    return render(request, 'viena_komanda.html', context=context_t)
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


class ZaidejasListView(generic.ListView):
    model = Zaidejas
    context_object_name = 'zaidejas_list'
    template_name = 'visi_zaidejai.html'

class ZaidejasDetailView(generic.DetailView):
    model = Zaidejas
    context_object_name = 'zaidejas'
    template_name = 'vienas_zaidejas.html'


def search(request):
    paieskos_tekstas = request.GET.get('laukelio-tekstas')
    paieskos_rezultatai = Zaidejas.objects.filter(
        Q(vardas__icontains=paieskos_tekstas) |
        Q(komanda__pavadinimas__icontains=paieskos_tekstas)
    )

    context_t = {
        'paieskos_tekstas_t': paieskos_tekstas,
        'paieskos_rezultatai_t': paieskos_rezultatai
    }
    return render(request, 'paieska.html', context=context_t)


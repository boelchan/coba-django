from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from ..forms import InsertForm, LaporanForm
from ..models import Laporan, Komentar, Vote


def index(request):
    context = {
        'title'   : 'laporan',
        'laporans': Laporan.objects.all(),
        'dicts'   : {'a': 'aaaa', 'b': 'bbbbbbb', 'c': 'ccccccc'}
    }
 
    return render(request, 'laporan/index.html', context)

def tambah(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = LaporanForm(request.POST)
            if form.is_valid():
                laporan_baru = form.save(commit=False)
                laporan_baru.pelapor = request.user
                laporan_baru.save()
                return HttpResponseRedirect('/')
        else:
            form = LaporanForm()

        return render(request, 'laporan/tambah.html', {'form': form})
    else:
        return HttpResponse('login dulu')
 
def laporan(request, laporan_id):
    lap = get_object_or_404(Laporan, pk=laporan_id)
    
    return HttpResponse(f'''
        <h1>Judul : {lap.judul}</h1>
        <h3>deskripsi : {lap.deskripsi}</h3>
    ''')

def kategori(request, kategori):
    return HttpResponse(f'kategori: {kategori}')

def kecamatan(request, kecamatan):
    return HttpResponse(f'kecamatan: {kecamatan}')

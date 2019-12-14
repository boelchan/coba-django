from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets

from .serializers import KategoriSerializers, KecamatanSerializers, KedinasanSerializers
from .models import Kategori, Kecamatan, Kedinasan


class KategoriRestView(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializers

class KecamatanRestView(viewsets.ModelViewSet):
    queryset = Kecamatan.objects.all()
    serializer_class = KecamatanSerializers

class KedinasanRestView(viewsets.ModelViewSet):
    queryset = Kedinasan.objects.all()
    serializer_class = KedinasanSerializers
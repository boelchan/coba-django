from django.http import JsonResponse
from rest_framework import viewsets, permissions
from helper import BlacklistPermission

from ..serializers import LaporanSerializers, KomentarSerializers, VoteSerializers
from ..models import Laporan, Komentar, Vote


def rest(request):
    data = {
        'id': 1,
        'name': 'tegar',
        'laporan': Laporan.objects.all()
    }
    return JsonResponse(data)

class LaporanRestView(viewsets.ModelViewSet):
    queryset = Laporan.objects.all()
    serializer_class = LaporanSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, BlacklistPermission)


class KomentarRestView(viewsets.ModelViewSet):
    queryset = Komentar.objects.all()
    serializer_class = KomentarSerializers

class VoteRestView(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializers

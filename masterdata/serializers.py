from rest_framework import serializers

from .models import Kategori, Kecamatan, Kedinasan

class KategoriSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class KecamatanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kecamatan
        fields = '__all__'

class KedinasanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kedinasan
        fields = '__all__'
from rest_framework import serializers

from .models import Laporan, Komentar, Vote, User

class KomentarSerializers(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    user = serializers.IntegerField(write_only=True)
    laporan = serializers.IntegerField(write_only=True)
  	
    class Meta:
        model = Komentar
        fields = '__all__'
    
    def create(self, validated_data):
        user_id = validated_data.pop('user')
        user = User.objects.get(id=user_id)
    
        laporan_id = validated_data.pop('laporan')
        laporan = Laporan.objects.get(id=laporan_id)
    
        komentar = Komentar.objects.create(user=user, 
                                            laporan=laporan,
                                            **validated_data)
        return komentar

    def update(self, instance, validated_data):
        print(instance)
        instance.komentar = validated_data.get('komentar')
        instance.save()
        
        return instance
        
        # user_id = validated_data.pop('user')
        # user = User.objects.get(id=user_id)
 
        # laporan_id = validated_data.pop('laporan')
        # laporan = Laporan.objects.get(id=laporan_id)
 
        # komentar = Komentar.objects.update(user=user, 
        #                                    laporan=laporan, 
        #                                    **validated_data)
        # return komentar

class VoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
        
class LaporanSerializers(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    daerah = serializers.CharField(source='daerah.nama')
    kategori = serializers.CharField(source='kategori.nama')
    pelapor = serializers.CharField(source='pelapor.username')
    komentar = KomentarSerializers(many=True, read_only=True)
    vote = VoteSerializers(many=True, read_only=True)
    class Meta:
        model = Laporan
        fields = '__all__'

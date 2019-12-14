from django.contrib import admin
from django.utils.html import format_html

from .models import Laporan, Komentar, Vote

class VoteInline(admin.TabularInline):
    model = Vote
    extra = 1

class KomentarInline(admin.TabularInline):
    model = Komentar
    extra = 1

class LaporanAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    inlines = (KomentarInline, VoteInline)
    
    list_display = (
        'timestamp',
        '__str__',
        'daerah',
        'kategori',
        'status',
        'lihat_map',
        'jumlah_komentar',
        'jumlah_vote_positif',
        'jumlah_vote_negatif'
    )
    

    def lihat_map(self, obj):
        return format_html(
            f'<a href="\
            https://www.google.com/maps/place/{obj.daerah}">\
            Lihat Map\
            </a>')

    list_display_links = ('__str__',)

    list_editable = ('status',)
    search_fields = ('judul', 'deskripsi')
    list_filter = ('timestamp', 'status')


class VoteAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    

admin.site.register(Laporan, LaporanAdmin)
admin.site.register(Komentar)
admin.site.register(Vote, VoteAdmin)
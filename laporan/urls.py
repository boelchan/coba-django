from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('laporan', views.LaporanRestView)
router.register('komentar', views.KomentarRestView)
router.register('vote', views.VoteRestView)


app_name = 'laporan'

urlpatterns = [
    path('', views.index, name='index'),
    path('laporan/<int:laporan_id>', views.laporan, name='laporan_detail'),
    path('laporan/tambah', views.tambah, name='laporan_tambah'),
    path('laporan/kategori/<kategori>', views.kategori, name='laporan_kategori'),
    path('laporan/kecamatan/<kecamatan>', views.kecamatan, name='laporan_kecamatan'),

    # api
    path('api/laoran_basic/', views.rest),
    path('api/laporan/', include(router.urls)),
]
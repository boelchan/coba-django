from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('kecamatan', views.KecamatanRestView)
router.register('kategori', views.KategoriRestView)
router.register('kedinasan', views.KedinasanRestView)

app_name = 'master'

urlpatterns = [
    # api
    path('api/master/', include(router.urls)),
]
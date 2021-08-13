from django.urls import path, register_converter
from . import views, converters

register_converter(converters.TanggalConverter, 'yyyy-mm-dd')

urlpatterns = [
    path("dataharian/", views.DataHarianList.as_view()),
    path("dataharian/<yyyy-mm-dd:tanggal>", views.DataHarianDetail.as_view()),
    path("datakecamatan/", views.DataPerKecamatanList.as_view()),
    path("datakecamatan/<yyyy-mm-dd:tanggal>", views.DataPerKecamatanDetail.as_view()),
]
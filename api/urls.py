from django.urls import path
from . import views

urlpatterns = [
    path('dataharian/', views.DataHarianList.as_view()),
    path('dataharian/<int:pk>', views.DataHarianList.as_view()),
    path('dataperkecamatan/', views.DataPerKecamatanList.as_view()),
    path('dataperkecamatan/<int:pk>', views.DataPerKecamatanList.as_view()),
]
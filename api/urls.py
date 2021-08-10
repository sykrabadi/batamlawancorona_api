from django.urls import path
from . import views

urlpatterns = [
    path('dataharian/', views.DataHarianList.as_view()),
]
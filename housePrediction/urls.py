from django.urls import path

from . import views


app_name = 'housePrediction'
urlpatterns = [
    path('', views.index, name='index'),
    path('estimate/', views.generateEstimate, name='estimate'),
]
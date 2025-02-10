from django.urls import path
from . import views

urlpatterns = [
    path('', views.buy_online, name='buy'),
    path('online/', views.buy_online, name='online'),
    path('in-person/', views.buy_in_person, name='in_person'),
]

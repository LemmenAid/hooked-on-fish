from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
    path('grounds/', views.grounds, name='grounds'),
]

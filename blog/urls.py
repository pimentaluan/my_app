from django.urls import path
from . import views

urlpatterns=[
    path('welcome/', views.welcome),
    path('eco/<mensagem>', views.eco),
    path('info/', views.info),
    
    path("home/", views.home, name="home"),
    path("contato/<int:numero>", views.contato, name="contato")
]
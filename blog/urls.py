from django.urls import path
from . import views

urlpatterns=[
    path('welcome/', views.welcome),
    path('eco/<mensagem>', views.eco),
    path('info/', views.info)
]
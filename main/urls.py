from django.urls import path
from . import views

#Отслеживание url адресов
urlpatterns = [
    path('', views.index, name='home'), # Отслеживание главной страницы
    path('about', views.about, name='about'),
    path('help', views.help, name='help'),
]

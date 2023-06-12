from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name='appHome'),
    path('category/',categores,name='category'),
]
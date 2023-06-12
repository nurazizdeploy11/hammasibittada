from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name='musicHome'),
    path('category/',categores,name='musiccategory'),
]
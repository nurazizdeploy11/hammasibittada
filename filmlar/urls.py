from django.urls import path
from .views import *
from .models import *
urlpatterns = [
    path('home/',home,name='tvHome'),
    path('category/',categores,name='filmcategory'),
    path('film/<int:pk>/',detail.as_view(),name="details"),
]
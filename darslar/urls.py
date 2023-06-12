from django.urls import path
from .views import *
from .models import *
urlpatterns = [
    path('home/',home,name='darsHome'),
    path('category/',categores,name='darscategory'),
]
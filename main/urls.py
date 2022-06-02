from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('price', price, name='price'),
    path('category/<num_cat>/', category, name='category'),
]
from django.urls import path
from .views import index, directores, dir_details

urlpatterns = [
    path('', index),
    path('directores/', directores),
    path('directores/<int:id>', dir_details),
]
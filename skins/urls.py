from django.urls import path
from .views import index, create

urlpatterns = [
    path('', index, name='skins_index'),
    path('create/', create, name='skins_create')
]

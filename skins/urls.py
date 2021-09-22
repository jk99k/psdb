from django.urls import path
from .views import index, detail, create, like, delete

urlpatterns = [
    path('', index, name='skins_index'),
    path('create/', create, name='skins_create'),
    path('detail/<int:pk>/', detail, name='skins_detail'),
    path('like/<int:pk>/',like, name='skins_like'),
    path('delete/<int:pk>/', delete, name='skins_delete'),
]

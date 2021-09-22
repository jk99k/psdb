from users.views import create, detail, edit, index
from django.urls import path

urlpatterns = [
    path('', index, name='users_index'),
    path('create/', create, name='users_create'),
    path('edit/', edit, name='users_edit'),
    path('detail/<str:username>/', detail, name='users_detail'),
]

from users.views import create, detail, index
from django.urls import path

urlpatterns = [
    path('', index, name='users_index'),
    path('create/', create, name='users_create'),
    path('detail/<str:username>/', detail, name='users_detail'),
]

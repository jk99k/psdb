from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as dj_logout
from .forms import UserCreateForm, UserLoginForm
from .models import User

def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/index.html', context)

def detail(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Http404('User does not exist')
    context = {'user': user}
    return render(request, 'users/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid(): 
            User.objects.create_user(**form.cleaned_data)
            authenticate(**form.cleaned_data)
            return redirect('http://localhost:8000/')
    else:
        form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})


def logout(request):
    dj_logout(request)
    return redirect('http://localhost:8000/')
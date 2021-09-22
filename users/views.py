from skins.models import Skin
from django.conf.urls import url
from django.http.response import Http404
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as dj_logout
from django.db.models import Q
from django.views.generic.edit import FormMixin
from .forms import UserCreateForm, UserEditForm
from .models import User

def index(request):
    query = request.GET.get('query')
    psid = request.GET.get('psid')

    if query:
        users = User.objects.filter(
            Q(username__icontains=query)
        )
    elif psid:
        users = User.objects.filter(
            pixel_strike_id=psid
        )
    else:
        users = User.objects.all()
    context = {
        'users': users,
        'current_user': request.user
    }
    return render(request, 'users/index.html', context)

def detail(request, username):
    try:
        user = User.objects.get(username=username)
        skins = Skin.objects.filter(author=user)
        client = user.client
    except User.DoesNotExist:
        return Http404('User does not exist')
    context = {
        'user': user,
        'current_user': request.user,
        'skins': skins,
        'client': client,
    }
    return render(request, 'users/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid(): 
            User.objects.create_user(**form.cleaned_data)
            user = authenticate(**form.cleaned_data)
            login(request, user)
            return redirect('http://localhost:8000/')
    else:
        form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})


def edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        form.save()
        return redirect('home')
    else:
        form = UserEditForm(instance=request.user)
        context = {
            'form': form,
            'current_user': request.user
        }
        return render(request, 'users/edit.html', context)

def logout(request):
    dj_logout(request)
    return redirect('http://localhost:8000/')
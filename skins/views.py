from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Like, Skin
from .forms import SkinCreateForm

# Create your views here.
def index(request):
    query = request.GET.get('query')
    skinid = request.GET.get('skinid')

    if query:
        skins = Skin.objects.filter(
            Q(name__icontains=query) | 
            Q(author__username__icontains=query) |
            Q(motif__icontains=query)
        )
    elif skinid:
        skins = Skin.objects.filter(
            skin_id=skinid
        )
    else:
        skins = Skin.objects.all()
    context = {
        'skins': skins,
        'current_user': request.user
    }

    return render(request, 'skins/index.html', context)

def detail(request, pk):
    skin = Skin.objects.get(pk=pk)
    likes_count = Like.objects.filter(skin=skin).count()
    is_author = skin.author == request.user
    context = {
        'skin': skin,
        'current_user': request.user,
        'likes_count': likes_count,
        'is_author': is_author,
    }
    return render(request, 'skins/detail.html', context)

@login_required
@transaction.atomic
def like(request, pk):
    skin = Skin.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            like = Like.objects.get(user=request.user, skin=skin)
            like.delete()
            skin.like_count -= 1
            skin.save()
            return redirect('skins_detail', pk)
        except Like.DoesNotExist:
            Like.objects.create(user=request.user, skin=skin)
            skin.like_count += 1
            skin.save()
            return redirect('skins_detail', pk)

@login_required
def create(request):
    if request.method == 'POST':
        form = SkinCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Skin.objects.create(author=request.user, **form.cleaned_data)
            return redirect('skins_index')
    else:
        form = SkinCreateForm()
        context = {
            'form': form,
            'current_user': request.user
        }
    return render(request, 'skins/create.html', context)

@login_required
def delete(request, pk):
    skin = Skin.objects.get(pk=pk)
    user = request.user
    if request.method == 'POST':
        if skin.author == user:
            skin.delete()
            print('success')
            return redirect('skins_index')
        else:
            print('no')
            return redirect('skins_index')
    else:
        print('not delete')
        return redirect('skins_index')
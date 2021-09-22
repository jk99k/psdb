from django.shortcuts import render
from skins.models import Skin
from django.contrib.auth import get_user_model

User = get_user_model()

def index(request):
    skins_top5 = Skin.objects.order_by('-like_count')[:5]
    creators_random = User.objects.order_by('?')[:5]
    context = {
        'skins': skins_top5,
        'users': creators_random,
        'current_user': request.user,
    }

    return render(request, 'basic/index.html', context)

def about(request):
    return render(request, 'basic/about.html')

def mod_r(request):
    return render(request, 'basic/mod-r.html')

def suggestions(request):
    return render(request, 'basic/suggestions.html')
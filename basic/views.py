from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'current_user': None
    }
    if request.user.is_authenticated:
        context['current_user'] = request.user

    return render(request, 'basic/index.html', context)
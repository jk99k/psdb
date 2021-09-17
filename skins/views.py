from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Skin
from .forms import SkinCreateForm

# Create your views here.
def index(request):
    skins = Skin.objects.all()
    context = {
        'skins': skins
    }

    return render(request, 'skins/index.html', context)

def create(request):
    if request.method == 'POST':
        form = SkinCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Skin.objects.create(author=request.user, **form.cleaned_data)
            return redirect('skins_index')
    else:
        form = SkinCreateForm()
    return render(request, 'skins/create.html', {'form': form})

# artworks/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artwork
from .forms import ArtworkForm, UserRegistrationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('artworks:artwork_list')  # Redirige vers la liste des œuvres d'art
    else:
        form = UserRegistrationForm()
    return render(request, 'artworks/register.html', {'form': form})

def artwork_list(request):
    artworks = Artwork.objects.all()
    return render(request, 'artworks/artwork_list.html', {'artworks': artworks})

def artwork_create(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)  # Inclut FILES pour les fichiers d'image
        if form.is_valid():
            form.save()
            return redirect('artworks:artwork_list')  # Redirige vers la liste des œuvres d'art
    else:
        form = ArtworkForm()
    return render(request, 'artworks/artwork_form.html', {'form': form})

def artwork_detail(request, pk):
    artwork = Artwork.objects.get(pk=pk)
    return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})

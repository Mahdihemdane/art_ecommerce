from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Artwork, Artist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ArtworkForm

class ArtworkListView(View):
    def get(self, request):
        artworks = Artwork.objects.all()
        return render(request, 'artworks/artwork_list.html', {'artworks': artworks})

class ArtworkDetailView(View):
    def get(self, request, pk):
        artwork = get_object_or_404(Artwork, pk=pk)
        return render(request, 'artworks/artwork_detail.html', {'artwork': artwork})

@method_decorator(login_required, name='dispatch')
class ArtworkCreateView(View):
    def get(self, request):
        form = ArtworkForm()
        return render(request, 'artworks/artwork_form.html', {'form': form})

    def post(self, request):
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.artist = Artist.objects.get(user=request.user)
            artwork.save()
            return redirect('artwork_list')
        return render(request, 'artworks/artwork_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ArtworkUpdateView(View):
    def get(self, request, pk):
        artwork = get_object_or_404(Artwork, pk=pk)
        form = ArtworkForm(instance=artwork)
        return render(request, 'artworks/artwork_form.html', {'form': form})

    def post(self, request, pk):
        artwork = get_object_or_404(Artwork, pk=pk)
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            return redirect('artwork_detail', pk=artwork.pk)
        return render(request, 'artworks/artwork_form.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class ArtworkDeleteView(View):
    def post(self, request, pk):
        artwork = get_object_or_404(Artwork, pk=pk)
        artwork.delete()
        return redirect('artwork_list')

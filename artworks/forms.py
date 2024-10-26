# artworks/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Artwork

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ('title', 'description', 'image')  # Adaptez ces champs à votre modèle Artwork

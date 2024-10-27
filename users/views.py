from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import UserProfile

class UserProfileView(View):
    def get(self, request):
        return render(request, 'users/user_profile.html', {'profile': request.user.userprofile})

class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='client')  # Default role
            login(request, user)
            return redirect('user_profile')
        return render(request, 'users/register.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile')
        return render(request, 'users/login.html', {'error': 'Invalid credentials'})

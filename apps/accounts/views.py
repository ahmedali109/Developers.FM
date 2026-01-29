from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserLoginForm

# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')


# Profile view
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

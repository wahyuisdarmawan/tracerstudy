from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST)
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'GET':
        return render(request, 'core/login.html', {
            'form': form
        })
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'User does not exiest.')
            return render(request, 'core/login.html', {
                'form': form
            })
        
def logout_view(request):
    logout(request)
    messages.success(request, 'You logged out')
    return redirect('core:login')
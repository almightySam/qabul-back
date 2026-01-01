from django.shortcuts import render, redirect
from .forms import PostForm, LoginForm
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView





def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')  # yoki success sahifaga
            else:
                messages.error(request, "Login yoki parol noto‘g‘ri")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})





def main(request):
    return render(request,'main.html')





def user_logout(request):
    logout(request)
    return redirect('login')
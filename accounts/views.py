
 
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate,login,logout


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        print('afdhjkdsal')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('home')

    return render(request, "accounts/form.html", {"form": form, 'title': 'Log in'})


def register_view(request):
    form_r= RegisterForm(request.POST or None)
    if form_r.is_valid():
        user = form_r.save(commit=False)
        password = form_r.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request,new_user)
        return redirect('home')
    return render(request, "accounts/form.html", {"form": form_r, 'title': 'Register'})


def logout_view(request):
    logout(request)
    return redirect('home')

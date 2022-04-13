from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def sign_up(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign in')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'auth/sign-up.html', context)


def sign_in(request):
    user = authenticate(username="plamen5", password="qwe")
    login(request, user)
    return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')

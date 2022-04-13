from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def create_account(request):
    pass

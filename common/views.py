from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView


# def index(request):
#     return render(request, 'index.html')
class IndexView(TemplateView):
    template_name = 'index.html'


def about(request):
    return render(request, 'common/about.html')


def contacts(request):
    return render(request, 'common/contacts.html')


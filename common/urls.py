from django.urls import path
from recipe_site.common import views

urlpatterns = [
    path('', views.index, name='index'),
]

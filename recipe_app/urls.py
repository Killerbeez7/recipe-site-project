from django.urls import path
from recipe_site.recipe_app import views

urlpatterns = (
    path('', views.list_recipes, name='list recipes'),
    path('add/', views.add_recipe, name='add recipe'),
)

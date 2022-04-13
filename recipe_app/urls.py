from django.urls import path
from recipe_site.recipe_app import views

urlpatterns = (
    path('create/', views.create_recipe, name='create recipe'),
)

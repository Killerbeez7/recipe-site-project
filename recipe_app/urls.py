from django.urls import path
from recipe_site.recipe_app import views

urlpatterns = (
    path('', views.RecipeListView.as_view(), name='list recipes'),
    path('add/', views.RecipeAddView.as_view(), name='add recipe'),
    path('details/', views.RecipeDetailsView.as_view(), name='recipe details'),
    # path('', views.list_recipes, name='list recipes'),
    # path('add/', views.add_recipe, name='add recipe'),
    # path('recipe-details/', views.recipe_details, name='recipe details'),
)

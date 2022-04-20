from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe


def list_recipes(request):
    recipes = Recipe.objects.all()
    for recipe in recipes:
        recipe.selected_image = recipe.recipeimage_set.filter(is_selected=True)\
            .first()

    context = {
        'recipes': recipes,
        'form': RecipeForm(),
    }

    return render(request, 'recipes/list_recipes.html', context)


def add_recipe(request):
    if request.method == 'GET':
        form = RecipeForm()
        return render(request, 'recipes/add_recipe.html', {'form': form})
    else:
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list recipes')

        return render(request, 'recipes/add_recipe.html', {'form': form})

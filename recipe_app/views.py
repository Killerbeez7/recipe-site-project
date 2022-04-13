from django.shortcuts import render, redirect
from .forms import RecipeCreateForm
from .models import Recipe


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeCreateForm()
        return render(request, 'recipes/create_recipe.html', {'form': form})
    else:
        form = RecipeCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'recipes/create_recipe.html', {'form': form})

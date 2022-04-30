from django.urls import reverse_lazy

from .models import Recipe
from django.views.generic import ListView, CreateView, DetailView

from ..core.mixins import AnyGroupRequiredMixin


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/list_recipes.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['recipe_images'] = RecipeImage
    #     return context


class RecipeAddView(AnyGroupRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'
    template_name = 'recipes/add_recipe.html'
    success_url = reverse_lazy('list recipes')


class RecipeDetailsView(DetailView):
    model = ''
    template_name = 'recipes/recipe_details.html'


# def list_recipes(request):
#     recipes = Recipe.objects.all()
#     for recipe in recipes:
#         recipe.selected_image = recipe.recipe_image_set.filter(is_selected=True)\
#             .first()
#
#     context = {
#         'recipes': recipes,
#         'form': RecipeForm(),
#     }
#
#     return render(request, 'recipes/list_recipes.html', context)


# @login_required(login_url=reverse_lazy('sign in'))
# @any_group_required(groups=['User'])
# def add_recipe(request):
#     if request.method == 'GET':
#         form = RecipeForm()
#         return render(request, 'recipes/add_recipe.html', {'form': form})
#     else:
#         form = RecipeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('list recipes')
#
#         return render(request, 'recipes/add_recipe.html', {'form': form})


# def recipe_details(request):
#     return render(request, 'recipes/recipe_details.html')

from django.contrib import admin

from recipe_site.recipe_app.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


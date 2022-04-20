from django.db import models


class Recipe(models.Model):
    name = models.CharField(
        max_length=30,
    )
    description = models.TextField(
        max_length=100,
    )


class RecipeImage(models.Model):
    image = models.ImageField(
        upload_to='recipes',
    )
    is_selected = models.BooleanField(
        default=False,
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

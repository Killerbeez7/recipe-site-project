from .models import Recipe, RecipeImage
from django import forms


class RecipeForm(forms.ModelForm):
    image = forms.ImageField()

    def save(self, commit=True):
        recipe = super().save(commit=commit)

        recipe_image = RecipeImage(
            image=self.cleaned_data['image'],
            recipe=recipe,
            is_selected=True,
        )

        if commit:
            recipe_image.save()

        return recipe

    class Meta:
        model = Recipe
        fields = '__all__'


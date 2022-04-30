from .models import Recipe
from django import forms


class RecipeForm(forms.ModelForm):
    def save(self, commit=True):
        recipe = super().save(commit=commit)

        recipe_image = Recipe(
            image=self.cleaned_data['image'],
            recipe=recipe,
            is_selected=True,
        )

        if commit:
            recipe_image.save()

        return recipe

    class Meta:
        model = Recipe
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.ImageField()
        }
        fields = '__all__'


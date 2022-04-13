from .models import Recipe
from django import forms


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
        fields = '__all__'

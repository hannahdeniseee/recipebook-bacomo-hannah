from django import forms
from .models import RecipeImage, Recipe


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']
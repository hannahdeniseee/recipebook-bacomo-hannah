from .models import Recipe, Ingredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_ingredients"] = self.object.ingredients.all()  # Fetch RecipeIngredient objects
        return context

class IngredientDetailView(DetailView):  
    model = Ingredient
    template_name = 'ingredient_detail.html'  
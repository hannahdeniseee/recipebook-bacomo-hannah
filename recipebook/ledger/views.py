from .models import Recipe, Ingredient, RecipeImage
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RecipeImageForm, RecipeForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

    def get_queryset(self):
        recipes = Recipe.objects.all()
        print("DEBUG: Recipes in queryset:", recipes)
        return recipes


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_ingredients"] = self.object.ingredients.all()
        return context


class IngredientDetailView(DetailView):  
    model = Ingredient
    template_name = 'ingredient_detail.html'


class AddRecipeImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'recipe_image.html'
    form_class = RecipeImageForm

    def form_valid(self, form):
        recipe_id = self.kwargs['pk'] 
        form.instance.recipe = Recipe.objects.get(pk=recipe_id)  
        return super().form_valid(form)


class AddRecipeView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'recipe_add.html'
    form_class = RecipeForm

    def form_valid(self, form):
        recipe_id = self.kwargs.get('pk') 
        form.instance.recipe = Recipe.objects.get(pk=recipe_id)  
        return super().form_valid(form)
from .models import Recipe, Ingredient
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


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


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/list"

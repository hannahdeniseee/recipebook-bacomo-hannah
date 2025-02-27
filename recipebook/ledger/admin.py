from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name',)  # Enable searching by name
    list_display = ('name',)  # Show only the name in the list view
    list_filter = ('name',)  # Allow filtering by name


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('recipe__name', 'ingredient__name')  # Search by recipe or ingredient name
    list_display = ('recipe', 'ingredient', 'quantity')  # Show these fields in the list view
    list_filter = ('recipe', 'ingredient')  # Allow filtering by recipe or ingredient


# Registering models with custom admin classes
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

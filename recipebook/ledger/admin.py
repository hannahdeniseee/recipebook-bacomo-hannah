from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created_on', 'updated_on')
    search_fields = ('name', 'author__username')  
    list_filter = ('created_on', 'updated_on')
    ordering = ('-created_on',)


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name',)
    list_display = ('name',)
    list_filter = ('name',)


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('recipe__name', 'ingredient__name')
    list_display = ('recipe', 'ingredient', 'quantity')
    list_filter = ('recipe', 'ingredient')


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

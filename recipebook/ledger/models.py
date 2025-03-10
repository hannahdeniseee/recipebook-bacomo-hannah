from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.id)])


class Recipe(models.Model): 
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.id)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='recipe')
  
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='ingredients')
   
    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"
   
  
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name

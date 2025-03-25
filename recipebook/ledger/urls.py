from django.urls import path
from .views import RecipeListView, RecipeDetailView
from .views import AddRecipeImageView, AddRecipeView

app_name = 'ledger'

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe-list'),
    path('<int:pk>/detail/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/add_image/',
         AddRecipeImageView.as_view(), name='add-recipe-image'),
    path('recipe/add/', AddRecipeView.as_view(), name='add-recipe'),
]

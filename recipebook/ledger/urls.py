from django.urls import path
from .views import RecipeListView, RecipeDetailView

app_name = 'ledger'

urlpatterns = [
    path('list', RecipeListView.as_view(), name='recipe-list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe-detail'),
]

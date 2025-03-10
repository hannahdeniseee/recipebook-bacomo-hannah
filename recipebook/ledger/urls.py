from django.urls import path, include
from .views import RecipeListView, RecipeDetailView, CustomLoginView

app_name = 'ledger'

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe-list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe-detail'),
    path("login/", CustomLoginView.as_view(), name="login"),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('ledger.urls', namespace="recipes")),
]

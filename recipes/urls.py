from django.urls import path
from . import views

urlpatterns = [
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("recipes/<int:pk>/", views.recipe_detail, name="recipe_detail"),
    path("recipes/generate/", views.generate_recipe, name="generate_recipe"),
]

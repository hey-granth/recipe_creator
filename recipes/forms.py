from django import forms
from .models import Ingredient, Recipe


class RecipeForm(forms.Form):
    """
    Form for creating or updating a recipe.
    """

    title = forms.CharField(max_length=100, label="Recipe Title")
    description = forms.CharField(widget=forms.Textarea, label="Description")
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Ingredients",
    )
    cuisine = forms.ChoiceField(choices=Recipe.cuisine_choices, label="Cuisine")
    dietary_restrictions = forms.ChoiceField(
        choices=Recipe.dietary_choices, label="Dietary Restrictions"
    )
    difficulty = forms.ChoiceField(
        choices=Recipe.difficulty_choices, label="Difficulty"
    )
    prep_time = forms.IntegerField(min_value=1, label="Preparation Time (minutes)")
    cook_time = forms.IntegerField(min_value=1, label="Cooking Time (minutes)")
    servings = forms.IntegerField(min_value=1, label="Number of Servings")
    allergens = forms.CharField(
        required=False, label="Allergens", help_text="Comma-separated list of allergens"
    )

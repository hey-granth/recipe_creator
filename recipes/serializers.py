from rest_framework import serializers
from .models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    instructions = serializers.CharField(required=False)

    class Meta:
        model = Recipe
        fields = "__all__"

    def create(self, validated_data):
        ingredients_data = validated_data.pop("ingredients", [])
        recipe = Recipe.objects.create(**validated_data)

        for ingredient_data in ingredients_data:
            name = str(ingredient_data.get("name", "")).strip().lower()
            unit = str(ingredient_data.get("unit", "")).strip().lower()
            quantity = str(ingredient_data.get("quantity", "")).strip().lower()

            ingredient = Ingredient.objects.filter(
                name=name, unit=unit, quantity=quantity
            ).first()

            if not ingredient:
                ingredient = Ingredient.objects.create(
                    name=name, unit=unit, quantity=quantity
                )

            recipe.ingredients.add(ingredient)

        return recipe

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from recipes.models import Ingredient, Recipe
from rest_framework.response import Response

class RecipeAPITests(APITestCase):

    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name="Tomato", quantity="2", unit="pieces")
        self.ingredient2 = Ingredient.objects.create(name="Pasta", quantity="200", unit="grams")

        self.valid_payload = {
            "title": "Tomato Pasta",
            "description": "Delicious tomato pasta",
            "ingredients": [
                {"name": "Tomato", "quantity": "2", "unit": "pieces"},
                {"name": "Pasta", "quantity": "200", "unit": "grams"}
            ],
            "cuisine": "italian",
            "dietary_restrictions": "vegan",
            "difficulty": "easy",
            "prep_time": 10,
            "cook_time": 20,
            "servings": 2
        }

    def test_generate_recipe_success(self):
        response = self.client.post(
            reverse("generate_recipe"),  # Make sure this matches your urls.py name
            data=self.valid_payload,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("instructions", response.data)
        self.assertEqual(response.data["title"], "Tomato Pasta")

    def test_generate_recipe_missing_field(self):
        incomplete_payload = self.valid_payload.copy()
        incomplete_payload.pop("title")

        response = self.client.post(
            reverse("generate_recipe"),
            data=incomplete_payload,
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("title", response.data)

    def test_recipe_list_endpoint(self):
        recipe = Recipe.objects.create(
            title="Sample",
            description="Test Recipe",
            instructions="Step 1: Do something",
            prep_time=5,
            cook_time=10,
            servings=1,
            cuisine="italian",
            dietary_restrictions="none",
            difficulty="easy"
        )
        recipe.ingredients.add(self.ingredient1, self.ingredient2)

        response = self.client.get(reverse("recipe_list"))  # Ensure this name exists in urls.py
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_ingredient_creation(self):
        Ingredient.objects.create(name="Onion", quantity="1", unit="piece")
        self.assertEqual(Ingredient.objects.count(), 3)

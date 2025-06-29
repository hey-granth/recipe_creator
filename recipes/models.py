from django.db import models
from django.db.models import JSONField


class Ingredient(models.Model):
    """
    A model representing an ingredient, including its name, quantity, unit, allergens, and cost per unit.
    """

    name: str = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit: str = models.CharField(max_length=50, blank=True, null=True)
    allergens: str = models.CharField(max_length=200, blank=True, null=True)
    cost_per_unit = models.DecimalField(
        blank=True, null=True, decimal_places=2, default=0.0, max_digits=1000
    )

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    """
    A model representing a recipe, including its ingredients, instructions, and nutritional information.
    """

    dietary_choices: list[tuple[str, str]] = [
        ("vegan", "Vegan"),
        ("vegetarian", "Vegetarian"),
        ("gluten_free", "Gluten Free"),
        ("dairy_free", "Dairy Free"),
        ("nut_free", "Nut Free"),
        ("halal", "Halal"),
        ("kosher", "Kosher"),
        ("paleo", "Paleo"),
        ("keto", "Keto"),
        ("low_carb", "Low Carb"),
        ("high_protein", "High Protein"),
        ("none", "None"),
    ]

    cuisine_choices: list[tuple[str, str]] = [
        ("indian", "Indian"),
        ("italian", "Italian"),
        ("mexican", "Mexican"),
        ("chinese", "Chinese"),
        ("japanese", "Japanese"),
        ("french", "French"),
        ("spanish", "Spanish"),
        ("other", "Other"),
    ]

    difficulty_choices: list[tuple[str, str]] = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    title: str = models.CharField(max_length=100)
    description: str = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    instructions: str = models.TextField(blank=True, null=True)
    dietary_restrictions: str = models.CharField(
        choices=dietary_choices, max_length=100, default="none"
    )
    cuisine: str = models.CharField(choices=cuisine_choices, max_length=30, default="none")
    difficulty: str = models.CharField(
        choices=difficulty_choices, max_length=10, default="easy"
    )
    prep_time: int = models.PositiveIntegerField(help_text="Preparation time in minutes")
    cook_time: int = models.PositiveIntegerField(help_text="Cooking time in minutes")
    servings: int = models.PositiveIntegerField(default=1)
    nutritional_info: JSONField = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def measure_ingredients(self, new_servings) -> None:
        """
        Measure the ingredients for a new number of servings.
        """
        factor: float = new_servings / self.servings
        for ingredient in self.ingredients.all():
            try:
                quantity = ingredient.quantity * factor
                ingredient.quantity = round(quantity, 2)

            except ValueError:
                continue

        self.servings = new_servings
        self.save()

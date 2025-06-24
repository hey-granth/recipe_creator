from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, blank=True, null=True)
    allergens = models.CharField(max_length=200, blank=True, null=True)
    cost_per_unit =models.DecimalField(blank=True, null=True, decimal_places=2, default=0.0, max_digits=1000)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    dietary_choices = [
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('gluten_free', 'Gluten Free'),
        ('dairy_free', 'Dairy Free'),
        ('nut_free', 'Nut Free'),
        ('halal', 'Halal'),
        ('kosher', 'Kosher'),
        ('paleo', 'Paleo'),
        ('keto', 'Keto'),
        ('low_carb', 'Low Carb'),
        ('high_protein', 'High Protein'),
        ('none', 'None'),
    ]

    cuisine_choices = [
        ('indian', 'Indian'),
        ('italian', 'Italian'),
        ('mexican', 'Mezican'),
        ('chinese', 'Chinese'),
        ('japanese', 'Japanese'),
        ('french', 'French'),
        ('spanish', 'Spanish'),
        ('other', 'Other'),
    ]

    difficulty_choices = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    dietary_restrictions = models.CharField(choices=dietary_choices, max_length=100, default='none')
    cuisine = models.CharField(choices=cuisine_choices, max_length=30, default='none')
    difficulty = models.CharField(choices=difficulty_choices, max_length=10, default='easy')
    prep_time = models.PositiveIntegerField(help_text="Preparation time in minutes")
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    servings = models.PositiveIntegerField(default=1)
    nutritional_info = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def measure_ingredients(self, new_servings):
        factor = new_servings / self.servings
        for ingredient in self.ingredients.all():
            try:
                quantity = ingredient.quantity * factor
                ingredient.quantity = round(quantity, 2)

            except ValueError:
                continue

        self.servings = new_servings
        self.save()
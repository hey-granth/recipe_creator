from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer
from .utils import get_nutritional_info, generate_recipe


@api_view(['GET'])
def recipe_list(request):
    """
    List all recipes.
    """
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def recipe_detail(request, pk):
    """
    Retrieve a specific recipe by its ID.
    """
    try:
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def generate_recipe(request):
    """
    Generate a recipe based on user input.
    """
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        ing_names = [ingredient['name'] for ingredient in request.data['ingredients']]
        cuisine = request.data.get('cuisine')
        diet = request.data.get('diet')
        difficulty = request.data.get('difficulty')

        # generating the recipe instructions and details from gemini
        ai_response = generate_recipe(
            ingredients=ing_names,
            cuisine=cuisine,
            diet=diet,
            difficulty=difficulty
        )
        if 'error' in ai_response:
            return Response({"error": ai_response['error']}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        recipe_object = serializer.save()
        nutritional_info = get_nutritional_info(recipe_object.ingredients.all())
        recipe_object.nutritional_info = nutritional_info
        recipe_object.instructions = ai_response.get('text', '')
        recipe_object.save()

        final_serializer = RecipeSerializer(recipe_object)
        return Response(final_serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
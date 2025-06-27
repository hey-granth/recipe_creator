from os import getenv
import requests
from google import genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_AI_STUDIO_API_KEY = getenv("GOOGLE_AI_STUDIO_API_KEY")
NUTRITIONIX_API_KEY = getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = getenv("NUTRITIONIX_APP_ID")

client = genai.Client(api_key=GOOGLE_AI_STUDIO_API_KEY)


# using the Google AI Studio API to generate a recipe based on user input
def generate_recipe_content(
    ingredients: list, cuisine: str, dietary_restrictions: str, difficulty: str
) -> dict[str, str]:
    """
    Generate a recipe using Google AI Studio API based on user input.
    """
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=(
                f"Generate a {difficulty} {cuisine} recipe for a {dietary_restrictions} diet "
                f"using ingredients: {', '.join(ingredients)}.\n\n"
                "Include:\n"
                "- Title\n"
                "- Description\n"
                "- Step-by-step instructions\n"
                "- Substitution suggestions\n"
                "- Serving tips"
            ),
        )

        return {"text": response.text}

    except Exception as e:
        return {"error": str(e)}


# using the Nutritionix API to get nutritional information for a recipe
def get_nutritional_info(ingredients: list) -> dict[str, str]:
    """
    Get nutritional information for a list of ingredients using the Nutritionix API.
    """
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "Content-Type": "application/json",
    }

    query = "\n".join(
        [f"{i.quantity} {i.name}" for i in ingredients if i.quantity and i.name]
    )
    data = {"query": query, "timezone": "Asia/Kolkata"}

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        return {"error": str(e)}

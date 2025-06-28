# 🧠 AI-Powered Recipe Generation System

This is a backend-only project built using Django and Django REST Framework (DRF), powered by Google AI (Gemini) for recipe generation and Nutritionix API for nutritional data.

## 🚀 Features

- Generate custom recipes based on ingredients, cuisine, diet, and difficulty.
- AI-generated instructions using Gemini API.
- Nutrition info from Nutritionix.
- Scalable and well-structured DRF backend.
- Fully API-based (no frontend dependency).
- Ready to connect with any frontend or mobile app.

## ⚙️ Technologies

- Django 4+
- Django REST Framework
- Python 3.8+
- Google AI Studio (Gemini)
- Nutritionix API
- SQLite (dev), PostgreSQL-ready (prod)

## 📁 API Endpoints

| Method | Endpoint                    | Description                          |
|--------|-----------------------------|--------------------------------------|
| POST   | /api/recipes/generate/      | Generate a recipe using AI & inputs |
| GET    | /api/recipes/               | List all generated recipes           |
| GET    | /api/recipes/{id}/          | View a specific recipe               |

## 🔑 Setup

### 1. Clone the Repo
```bash
git clone https://github.com/hey-granth/recipe_creator.git
cd recipe_creator
```

### 2. Install Dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file with the following:
```
GOOGLE_API_KEY=your-google-api-key
NUTRITIONIX_APP_ID=your-app-id
NUTRITIONIX_APP_KEY=your-app-key
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
```

## 📄 Sample Payload

POST `/api/recipes/generate/`

```json
{
  "title": "Custom Recipe",
  "description": "Healthy and tasty!",
  "ingredients": [
    { "name": "potato", "quantity": "2", "unit": "pieces" },
    { "name": "onion", "quantity": "1", "unit": "medium" }
  ],
  "cuisine": "indian",
  "dietary_restrictions": "vegan",
  "difficulty": "easy",
  "servings": 2,
  "prep_time": 10,
  "cook_time": 20
}
```

## 📚 Dietary Options Supported

- Vegan
- Vegetarian
- Gluten Free
- Dairy Free
- Nut Free
- Halal
- Kosher
- Paleo
- Keto
- Low Carb
- High Protein
- None

## 🧪 Running Tests

```bash
python manage.py test recipes
```

## 👨‍💻 Developer

**Granth Agarwal**  
[GitHub](https://github.com/hey-granth) | [LinkedIn](https://linkedin.com/in/granth-agarwal) | [Twitter](https://twitter.com/heygranth)

---
# Recipe Creator API Documentation

## Overview

The Recipe Creator API is a Django REST Framework-based service that allows users to create, retrieve, and manage recipes with ingredients. The API supports AI-powered recipe generation with nutritional information and various dietary restrictions.

**Base URL:** `http://your-domain.com/api/`

**API Documentation:** Available at `/api/docs/` (Swagger UI)

**API Schema:** Available at `/api/schema/`

## Authentication

Currently, the API does not require authentication for any endpoints.

## Data Models

### Ingredient

Represents an ingredient with its nutritional and cost information.

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `id` | Integer | Unique identifier | Auto-generated |
| `name` | String | Ingredient name (max 100 chars) | Yes |
| `quantity` | Decimal | Quantity amount (max 10 digits, 2 decimal places) | Yes |
| `unit` | String | Unit of measurement (max 50 chars) | No |
| `allergens` | String | Allergen information (max 200 chars) | No |
| `cost_per_unit` | Decimal | Cost per unit (max 1000 digits, 2 decimal places) | No |

### Recipe

Represents a complete recipe with ingredients, instructions, and metadata.

| Field | Type | Description | Required |
|-------|------|-------------|----------|
| `id` | Integer | Unique identifier | Auto-generated |
| `title` | String | Recipe title (max 100 chars) | Yes |
| `description` | Text | Recipe description | Yes |
| `ingredients` | Array | List of ingredient objects | Yes |
| `instructions` | Text | Step-by-step cooking instructions | No |
| `dietary_restrictions` | String | Dietary category | No (default: "none") |
| `cuisine` | String | Cuisine type | No (default: "none") |
| `difficulty` | String | Cooking difficulty level | No (default: "easy") |
| `prep_time` | Integer | Preparation time in minutes | Yes |
| `cook_time` | Integer | Cooking time in minutes | Yes |
| `servings` | Integer | Number of servings | No (default: 1) |
| `nutritional_info` | JSON | Nutritional information object | No |
| `created_at` | DateTime | Creation timestamp | Auto-generated |

#### Dietary Restrictions Options
- `vegan` - Vegan
- `vegetarian` - Vegetarian
- `gluten_free` - Gluten Free
- `dairy_free` - Dairy Free
- `nut_free` - Nut Free
- `halal` - Halal
- `kosher` - Kosher
- `paleo` - Paleo
- `keto` - Keto
- `low_carb` - Low Carb
- `high_protein` - High Protein
- `none` - None

#### Cuisine Options
- `indian` - Indian
- `italian` - Italian
- `mexican` - Mexican
- `chinese` - Chinese
- `japanese` - Japanese
- `french` - French
- `spanish` - Spanish
- `other` - Other

#### Difficulty Options
- `easy` - Easy
- `medium` - Medium
- `hard` - Hard

## Endpoints

### 1. List All Recipes

Retrieve a list of all recipes in the system.

**Endpoint:** `GET /api/recipes/`

**Response:**
- **Status Code:** 200 OK
- **Content-Type:** application/json

**Response Body:**
```json
[
  {
    "id": 1,
    "title": "Spaghetti Carbonara",
    "description": "Classic Italian pasta dish",
    "ingredients": [
      {
        "id": 1,
        "name": "Spaghetti",
        "quantity": "400.00",
        "unit": "grams",
        "allergens": "gluten",
        "cost_per_unit": "0.50"
      }
    ],
    "instructions": "Detailed cooking instructions...",
    "dietary_restrictions": "none",
    "cuisine": "italian",
    "difficulty": "medium",
    "prep_time": 15,
    "cook_time": 20,
    "servings": 4,
    "nutritional_info": {
      "calories": 450,
      "protein": "18g",
      "carbs": "65g",
      "fat": "15g"
    },
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

### 2. Get Recipe Details

Retrieve detailed information about a specific recipe.

**Endpoint:** `GET /api/recipes/{id}/`

**Path Parameters:**
- `id` (integer): Recipe ID

**Response:**
- **Status Code:** 200 OK (success)
- **Status Code:** 404 Not Found (recipe doesn't exist)
- **Content-Type:** application/json

**Success Response Body:**
```json
{
  "id": 1,
  "title": "Spaghetti Carbonara",
  "description": "Classic Italian pasta dish",
  "ingredients": [
    {
      "id": 1,
      "name": "Spaghetti",
      "quantity": "400.00",
      "unit": "grams",
      "allergens": "gluten",
      "cost_per_unit": "0.50"
    }
  ],
  "instructions": "Detailed cooking instructions...",
  "dietary_restrictions": "none",
  "cuisine": "italian",
  "difficulty": "medium",
  "prep_time": 15,
  "cook_time": 20,
  "servings": 4,
  "nutritional_info": {
    "calories": 450,
    "protein": "18g",
    "carbs": "65g",
    "fat": "15g"
  },
  "created_at": "2024-01-15T10:30:00Z"
}
```

**Error Response Body:**
```json
{
  "error": "Recipe not found"
}
```

### 3. Generate Recipe

Create a new recipe using AI-powered generation based on provided ingredients and preferences.

**Endpoint:** `POST /api/recipes/generate/`

**Request Headers:**
- `Content-Type: application/json`

**Request Body:**
```json
{
  "title": "My Custom Recipe",
  "description": "A delicious homemade meal",
  "ingredients": [
    {
      "name": "Chicken Breast",
      "quantity": "500.00",
      "unit": "grams",
      "allergens": "",
      "cost_per_unit": "8.00"
    },
    {
      "name": "Rice",
      "quantity": "200.00",
      "unit": "grams",
      "allergens": "",
      "cost_per_unit": "2.00"
    }
  ],
  "dietary_restrictions": "high_protein",
  "cuisine": "italian",
  "difficulty": "medium",
  "prep_time": 20,
  "cook_time": 30,
  "servings": 2
}
```

**Response:**
- **Status Code:** 201 Created (success)
- **Status Code:** 400 Bad Request (validation errors)
- **Status Code:** 500 Internal Server Error (AI generation failed)
- **Content-Type:** application/json

**Success Response Body:**
```json
{
  "id": 2,
  "title": "My Custom Recipe",
  "description": "A delicious homemade meal",
  "ingredients": [
    {
      "id": 2,
      "name": "Chicken Breast",
      "quantity": "500.00",
      "unit": "grams",
      "allergens": "",
      "cost_per_unit": "8.00"
    },
    {
      "id": 3,
      "name": "Rice",
      "quantity": "200.00",
      "unit": "grams",
      "allergens": "",
      "cost_per_unit": "2.00"
    }
  ],
  "instructions": "AI-generated step-by-step cooking instructions...",
  "dietary_restrictions": "high_protein",
  "cuisine": "italian",
  "difficulty": "medium",
  "prep_time": 20,
  "cook_time": 30,
  "servings": 2,
  "nutritional_info": {
    "calories": 620,
    "protein": "45g",
    "carbs": "55g",
    "fat": "12g"
  },
  "created_at": "2024-01-15T11:00:00Z"
}
```

**Validation Error Response:**
```json
{
  "field_name": [
    "This field is required."
  ]
}
```

**AI Generation Error Response:**
```json
{
  "error": "Failed to generate recipe content"
}
```

## Request/Response Examples

### Creating a Simple Vegetarian Recipe

**Request:**
```bash
curl -X POST http://your-domain.com/api/recipes/generate/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Vegetable Stir Fry",
    "description": "Quick and healthy vegetable stir fry",
    "ingredients": [
      {
        "name": "Bell Peppers",
        "quantity": "2.00",
        "unit": "pieces",
        "allergens": "",
        "cost_per_unit": "1.50"
      },
      {
        "name": "Broccoli",
        "quantity": "300.00",
        "unit": "grams",
        "allergens": "",
        "cost_per_unit": "2.00"
      }
    ],
    "dietary_restrictions": "vegetarian",
    "cuisine": "chinese",
    "difficulty": "easy",
    "prep_time": 10,
    "cook_time": 15,
    "servings": 2
  }'
```

### Retrieving All Recipes

**Request:**
```bash
curl -X GET http://your-domain.com/api/recipes/
```

### Getting Specific Recipe

**Request:**
```bash
curl -X GET http://your-domain.com/api/recipes/1/
```

## Error Handling

The API uses standard HTTP status codes and returns error messages in JSON format:

| Status Code | Description |
|-------------|-------------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid request data |
| 404 | Not Found - Requested resource not found |
| 500 | Internal Server Error - Server error occurred |

## Features

### AI-Powered Recipe Generation
The `/api/recipes/generate/` endpoint uses AI (Gemini) to automatically generate cooking instructions based on the provided ingredients and preferences.

### Automatic Nutritional Information
When generating recipes, the system automatically calculates and includes nutritional information for the recipe.

### Ingredient Management
Ingredients are managed separately and can be reused across multiple recipes. The system uses get_or_create to avoid duplicate ingredients.

### Recipe Scaling
The Recipe model includes a `measure_ingredients()` method that can adjust ingredient quantities based on the desired number of servings.

## Notes

- All decimal fields support up to 2 decimal places for precision
- Timestamps are automatically generated and returned in ISO 8601 format
- The API supports nested ingredient creation within recipe generation
- Nutritional information is stored as flexible JSON data
- The system integrates with external AI services for recipe generation

## Integration Examples

### Frontend Integration
```javascript
// Fetch all recipes
fetch('/api/recipes/')
  .then(response => response.json())
  .then(data => console.log(data));

// Generate a new recipe
fetch('/api/recipes/generate/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: 'My Recipe',
    description: 'Delicious meal',
    ingredients: [/* ingredient objects */],
    dietary_restrictions: 'vegetarian',
    cuisine: 'italian',
    difficulty: 'easy',
    prep_time: 15,
    cook_time: 25,
    servings: 4
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

This API provides a complete solution for recipe management with AI-powered content generation and comprehensive nutritional information.
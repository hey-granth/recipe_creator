// DOM Elements
const DOM = {
    form: document.getElementById('recipeForm'),
    generateBtn: document.getElementById('generateBtn'),
    loader: document.getElementById('loader'),
    btnText: document.getElementById('btnText'),
    errorMessage: document.getElementById('errorMessage'),
    responseSection: document.getElementById('responseSection'),
    recipeTitle: document.getElementById('recipeTitle'),
    ingredientsList: document.getElementById('recipeIngredients'),
    instructionsContainer: document.getElementById('recipeInstructions'),
    nutritionDiv: document.getElementById('nutritionInfo'),
    ingredientsInput: document.getElementById('ingredients'),
    cuisineSelect: document.getElementById('cuisine'),
    dietarySelect: document.getElementById('dietary'),
    difficultySelect: document.getElementById('difficulty'),
    servingsInput: document.getElementById('servings'),
    prepTimeInput: document.getElementById('prepTime'),
    cookTimeInput: document.getElementById('cookTime'),
};

// Form validation
function validateForm(formData) {
    const errors = [];

    if (!Array.isArray(formData.ingredients) || formData.ingredients.length === 0) {
        errors.push('At least one ingredient is required.');
    }

    if (!formData.cuisine) {
        errors.push('Please select a cuisine.');
    }

    if (!formData.difficulty) {
        errors.push('Please select a difficulty level.');
    }

    if (!formData.servings || formData.servings < 1 || formData.servings > 20) {
        errors.push('Servings must be between 1 and 20.');
    }

    if (!formData.prep_time || formData.prep_time < 1 || formData.prep_time > 300) {
        errors.push('Prep time must be between 1 and 300 minutes.');
    }

    if (!formData.cook_time || formData.cook_time < 1 || formData.cook_time > 480) {
        errors.push('Cook time must be between 1 and 480 minutes.');
    }

    return errors;
}

// Show error message
function showError(message) {
    DOM.errorMessage.textContent = message;
    DOM.errorMessage.style.display = 'block';
    setTimeout(() => {
        DOM.errorMessage.style.display = 'none';
    }, 5000);
}

// Toggle loading state
function toggleLoading(isLoading) {
    DOM.generateBtn.disabled = isLoading;
    DOM.loader.style.display = isLoading ? 'inline-block' : 'none';
    DOM.btnText.textContent = isLoading ? 'Generating...' : 'Generate Recipe';
}

// Format ingredient for display
function formatIngredient(ingredient) {
    const { name, quantity, unit } = ingredient;
    const quantityStr = quantity || '';
    const unitStr = unit && unit !== 'piece' ? unit : '';
    return `${quantityStr}${unitStr ? ` ${unitStr} ` : ' '}${name}`.trim();
}

// Display recipe
function displayRecipe(recipe) {
    DOM.recipeTitle.textContent = recipe.title || 'Untitled Recipe';
    DOM.ingredientsList.innerHTML = '';
    if (Array.isArray(recipe.ingredients)) {
        recipe.ingredients.forEach(ingredient => {
            const li = document.createElement('li');
            li.textContent = formatIngredient(ingredient);
            DOM.ingredientsList.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = 'No ingredients available';
        DOM.ingredientsList.appendChild(li);
    }

    DOM.instructionsContainer.innerHTML = recipe.instructions
        ? marked.parse(recipe.instructions)
        : '<p>No instructions provided.</p>';

    DOM.nutritionDiv.innerHTML = '';
    if (recipe.nutritional_info && typeof recipe.nutritional_info === 'object') {
        Object.entries(recipe.nutritional_info).forEach(([key, value]) => {
            const div = document.createElement('div');
            div.className = 'nutrition-item';
            div.innerHTML = `
        <strong>${value}</strong>
        <span>${key.replace(/_/g, ' ').replace(/\b\fol/g, c => c.toUpperCase())}</span>
      `;
            DOM.nutritionDiv.appendChild(div);
        });
    } else {
        DOM.nutritionDiv.innerHTML = '<p>No nutritional information available.</p>';
    }

    console.log('Recipe data:', recipe);
    console.log('Nutritional info:', recipe.nutritional_info);
    DOM.responseSection.style.display = 'block';
}

// API call to generate recipe
async function generateRecipe(formData) {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/recipes/generate/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('Serializer errors:', errorData);
            throw new Error(
                errorData.errors
                    ? JSON.stringify(errorData.errors)
                    : `HTTP error! Status: ${response.status}`
            );
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('API error:', error);
        throw new Error(
            error.message.includes('HTTP error')
                ? error.message
                : 'Failed to generate recipe. Please check the form data and try again.'
        );
    }
}

// Get form data
function getFormData() {
    const rawIngredients = DOM.ingredientsInput.value;
    const ingredientsArray = rawIngredients
        .split(',')
        .map(item => item.trim())
        .filter(item => item.length > 0)
        .map(name => ({
            name,
            quantity: 1,
            unit: 'piece',
        }));

    return {
        title: 'Generated Recipe',
        description: 'AI-generated custom recipe',
        ingredients: ingredientsArray,
        cuisine: DOM.cuisineSelect.value,
        dietary_restrictions: DOM.dietarySelect.value || 'none',
        difficulty: DOM.difficultySelect.value,
        servings: parseInt(DOM.servingsInput.value, 10) || 1,
        prep_time: parseInt(DOM.prepTimeInput.value, 10) || 1,
        cook_time: parseInt(DOM.cookTimeInput.value, 10) || 1,
    };
}

// Form submit handler
DOM.form.addEventListener('submit', async (e) => {
    e.preventDefault();
    DOM.errorMessage.style.display = 'none';
    DOM.responseSection.style.display = 'none';

    const formData = getFormData();
    const errors = validateForm(formData);

    if (errors.length > 0) {
        showError(errors.join(' '));
        return;
    }

    try {
        toggleLoading(true);
        const recipe = await generateRecipe(formData);
        displayRecipe(recipe);
    } catch (error) {
        showError(error.message);
    } finally {
        toggleLoading(false);
    }
});

// Add smooth hover effects
document.querySelectorAll('.form-group input, .form-group select, .form-group textarea').forEach(element => {
    element.addEventListener('focus', () => {
        element.parentElement.style.transform = 'translateY(-2px)';
    });
    element.addEventListener('blur', () => {
        element.parentElement.style.transform = 'translateY(0)';
    });
});
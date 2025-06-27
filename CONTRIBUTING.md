# Contributing to Recipe Creator API

Thank you for your interest in contributing to the Recipe Creator API! We welcome contributions from developers of all skill levels. This guide will help you get started with contributing to our project.

## 🤝 How to Contribute

There are many ways you can contribute to this project:

- **Bug Reports**: Help us identify and fix issues
- **Feature Requests**: Suggest new functionality
- **Code Contributions**: Submit bug fixes or new features
- **Documentation**: Improve or add to our documentation
- **Testing**: Help improve test coverage
- **Code Review**: Review pull requests from other contributors

## 📋 Before You Start

### Code of Conduct

By participating in this project, you agree to abide by our code of conduct:

- **Be respectful**: Treat all community members with respect and kindness
- **Be inclusive**: Welcome newcomers and help them learn
- **Be collaborative**: Work together to solve problems
- **Be patient**: Remember that everyone has different skill levels and backgrounds
- **Be constructive**: Provide helpful feedback and suggestions

### Prerequisites

Before contributing, ensure you have:

- Python 3.8+ installed
- Git installed and configured
- Basic knowledge of Django and Django REST Framework
- Understanding of RESTful API principles
- Familiarity with the project structure (see README.md)

## 🚀 Getting Started

### 1. Fork and Clone the Repository

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/recipe-creator-api.git
cd recipe-creator-api

# Add the original repository as upstream
git remote add upstream https://github.com/ORIGINAL_OWNER/recipe-creator-api.git
```

### 2. Set Up Development Environment

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if you create a requirements-dev.txt)
pip install -r requirements-dev.txt
```

### 3. Create Environment File

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
# Make sure to add your Gemini API key for testing AI features
```

### 4. Set Up Database

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create test data (optional)
python manage.py createsuperuser
```

### 5. Run Tests

```bash
# Run the test suite to ensure everything works
python manage.py test

# Run with coverage (recommended)
coverage run manage.py test
coverage report
```

## 🐛 Reporting Issues

### Before Submitting an Issue

1. **Search existing issues** to avoid duplicates
2. **Check the documentation** to ensure it's not a usage question
3. **Test with the latest version** to see if the issue still exists

### How to Submit a Good Bug Report

Include the following information:

```markdown
## Bug Description
A clear and concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g. Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g. 3.9.7]
- Django Version: [e.g. 5.2.3]
- Browser (if applicable): [e.g. Chrome 91.0]

## Additional Context
Add any other context about the problem here.
Screenshots, error logs, etc.
```

## 💡 Suggesting Features

### Before Submitting a Feature Request

1. **Check existing issues** for similar requests
2. **Consider the scope** - does it fit the project's goals?
3. **Think about implementation** - is it technically feasible?

### Feature Request Template

```markdown
## Feature Description
A clear and concise description of the feature you'd like to see.

## Problem Statement
What problem does this feature solve?

## Proposed Solution
How would you like this feature to work?

## Alternative Solutions
Have you considered any alternative approaches?

## Additional Context
Any other context, mockups, or examples.
```

## 🔧 Development Guidelines

### Code Style and Standards

We use **Ruff** for code linting and formatting:

```bash
# Check code style
ruff check .

# Fix auto-fixable issues
ruff check . --fix

# Format code
ruff format .
```

### Code Standards

- **Follow PEP 8**: Use Python's official style guide
- **Use meaningful names**: Variables, functions, and classes should have descriptive names
- **Write docstrings**: All public functions and classes should have docstrings
- **Keep functions small**: Aim for functions that do one thing well
- **Use type hints**: Add type hints for function parameters and return values

### Example Code Style

```python
from typing import List, Optional
from django.db import models
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ingredient model.
    
    Handles serialization/deserialization of ingredient data
    including validation of quantity and cost fields.
    """
    
    class Meta:
        model = Ingredient
        fields = '__all__'
    
    def validate_quantity(self, value: float) -> float:
        """Validate that quantity is positive."""
        if value <= 0:
            raise serializers.ValidationError(
                "Quantity must be greater than zero."
            )
        return value
```

### Database Migrations

When making model changes:

```bash
# Create migrations
python manage.py makemigrations

# Check migration before applying
python manage.py sqlmigrate recipes 0001

# Apply migrations
python manage.py migrate
```

### Testing Guidelines

- **Write tests for new features**: All new functionality should include tests
- **Maintain test coverage**: Aim for at least 80% test coverage
- **Test edge cases**: Include tests for error conditions and boundary cases
- **Use descriptive test names**: Test names should clearly describe what they test

#### Test Structure

```python
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Recipe, Ingredient


class RecipeAPITestCase(TestCase):
    """Test cases for Recipe API endpoints."""
    
    def setUp(self):
        """Set up test data."""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.ingredient = Ingredient.objects.create(
            name='Test Ingredient',
            quantity=100.0,
            unit='grams'
        )
    
    def test_create_recipe_success(self):
        """Test successful recipe creation."""
        data = {
            'title': 'Test Recipe',
            'description': 'A test recipe',
            'ingredients': [self.ingredient.id],
            'prep_time': 15,
            'cook_time': 30,
            'servings': 4
        }
        
        response = self.client.post('/api/recipes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)
```

## 📝 Submitting Changes

### Branch Naming Convention

Use descriptive branch names:

- **Feature**: `feature/add-recipe-search`
- **Bug Fix**: `bugfix/fix-ingredient-validation`
- **Documentation**: `docs/update-api-documentation`
- **Refactor**: `refactor/optimize-database-queries`

### Commit Message Guidelines

Follow the conventional commit format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Build process or auxiliary tool changes

**Examples:**
```bash
feat(api): add recipe search functionality

Add endpoint to search recipes by ingredients, cuisine type,
and dietary restrictions. Includes pagination and sorting options.

Closes #123

fix(serializer): validate ingredient quantities properly

Ensure that ingredient quantities are positive numbers
and handle decimal precision correctly.

docs(readme): update installation instructions

Add missing steps for environment setup and clarify
database configuration options.
```

### Pull Request Process

1. **Update your fork**:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   ```

2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**:
    - Write code following our style guidelines
    - Add tests for new functionality
    - Update documentation as needed
    - Ensure all tests pass

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
    - Use the pull request template
    - Provide a clear description of changes
    - Link to related issues
    - Request reviews from maintainers

### Pull Request Template

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Related Issues
Closes #(issue number)

## Testing
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] I have tested the API endpoints manually

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] Any dependent changes have been merged and published
```

## 🔍 Code Review Process

### For Contributors

- **Be responsive**: Address feedback promptly
- **Ask questions**: Don't hesitate to ask for clarification
- **Be open to feedback**: View code review as a learning opportunity
- **Test thoroughly**: Ensure your changes work as expected

### For Reviewers

- **Be constructive**: Provide helpful, actionable feedback
- **Be thorough**: Check for bugs, performance issues, and code quality
- **Be timely**: Review pull requests in a reasonable timeframe
- **Be encouraging**: Recognize good work and improvements

## 🏗️ Project Architecture

### Key Components

- **Models** (`models.py`): Database structure and business logic
- **Views** (`views.py`): API endpoints and request handling
- **Serializers** (`serializers.py`): Data validation and transformation
- **Utils** (`utils.py`): Helper functions and external integrations

### Design Principles

- **Single Responsibility**: Each class/function should have one clear purpose
- **DRY (Don't Repeat Yourself)**: Avoid code duplication
- **SOLID Principles**: Follow object-oriented design principles
- **API Design**: Follow RESTful conventions and HTTP standards

## 🧪 Testing Strategy

### Test Categories

1. **Unit Tests**: Test individual functions and methods
2. **Integration Tests**: Test component interactions
3. **API Tests**: Test HTTP endpoints and responses
4. **Performance Tests**: Test system performance under load

### Test Coverage Goals

- **Overall Coverage**: Minimum 80%
- **Critical Paths**: 100% coverage for core functionality
- **Edge Cases**: Include boundary and error conditions

## 📚 Documentation

### Types of Documentation

- **Code Comments**: Explain complex logic
- **Docstrings**: Document public APIs
- **README**: Project overview and setup
- **API Documentation**: Endpoint specifications
- **Contributing Guide**: This document

### Documentation Standards

- **Clear and Concise**: Use simple, direct language
- **Examples**: Include practical examples
- **Up-to-date**: Keep documentation current with code changes
- **Accessible**: Consider different skill levels

## 🚀 Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist

- [ ] All tests pass
- [ ] Documentation updated
- [ ] Version number bumped
- [ ] Changelog updated
- [ ] Security review completed
- [ ] Performance testing completed

## 📞 Getting Help

### Communication Channels

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Pull Request Comments**: For code-specific discussions

### Documentation Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Python Style Guide (PEP 8)](https://pep8.org/)

## 🙏 Recognition

Contributors will be recognized in:

- **README.md**: Contributors section
- **Release Notes**: Major contribution acknowledgments
- **GitHub**: Contributor statistics and graphs

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing to Recipe Creator API! Your efforts help make this project better for everyone. 🎉
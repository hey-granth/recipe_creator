# Generated by Django 5.2.3 on 2025-06-27 05:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_alter_recipe_instructions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]

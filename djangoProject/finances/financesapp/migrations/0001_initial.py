# Generated by Django 4.2.15 on 2024-09-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SignIn",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("login", models.CharField(max_length=30, unique=True)),
                ("passwd", models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="SignUp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=30, unique=True)),
                ("password", models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]

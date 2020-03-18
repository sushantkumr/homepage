# Generated by Django 3.0.4 on 2020-03-17 07:42

import django.core.validators
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID",),),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified",
                    ),
                ),
                (
                    "key",
                    models.CharField(
                        max_length=20,
                        validators=[django.core.validators.MinLengthValidator(1)],
                        verbose_name="Label of the item",
                    ),
                ),
                (
                    "value",
                    models.TextField(
                        validators=[django.core.validators.MinLengthValidator(1)], verbose_name="Value of the item",
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        choices=[("bookmark", "Bookmark")],
                        default="bookmark",
                        max_length=20,
                        verbose_name="Type of item",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]

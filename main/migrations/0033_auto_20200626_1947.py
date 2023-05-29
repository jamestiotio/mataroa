# Generated by Django 3.0.7 on 2020-06-26 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0032_auto_20200620_1431"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterField(
            model_name="user",
            name="footer_note",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="Supports markdown",
                max_length=500,
                null=True,
            ),
        ),
    ]

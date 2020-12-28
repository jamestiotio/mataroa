# Generated by Django 3.1 on 2020-12-28 15:35

from django.db import migrations, models

import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0048_auto_20201218_1351"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="redirect_domain",
            field=models.CharField(
                blank=True,
                help_text="Retiring your mataroa blog? We can redirect to your domain.",
                max_length=150,
                null=True,
                validators=[main.validators.validate_domain_name],
            ),
        ),
    ]

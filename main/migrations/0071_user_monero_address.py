# Generated by Django 4.0.2 on 2022-02-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0070_notificationrecord_is_canceled"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="monero_address",
            field=models.CharField(blank=True, max_length=95, null=True),
        ),
    ]

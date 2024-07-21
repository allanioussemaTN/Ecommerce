# Generated by Django 5.0.7 on 2024-07-18 14:46

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_profile_location"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="name",
        ),
        migrations.AddField(
            model_name="profile",
            name="birthday",
            field=models.DateField(
                blank=True,
                help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(default="", max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="first_name",
            field=models.CharField(default="", max_length=120),
        ),
        migrations.AddField(
            model_name="profile",
            name="last_name",
            field=models.CharField(default="", max_length=120),
        ),
        migrations.AddField(
            model_name="profile",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                help_text="Enter phone number with country code.",
                max_length=128,
                null=True,
                region=None,
                unique=True,
            ),
        ),
        migrations.AddField(
            model_name="profile",
            name="sum_purchase",
            field=models.CharField(default="", max_length=120),
        ),
    ]

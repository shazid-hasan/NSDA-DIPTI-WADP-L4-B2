# Generated by Django 5.0.3 on 2024-03-21 21:32

import Portfolio.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_userprofile_carrer_obj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(null=True, validators=[Portfolio.models.validate_age]),
        ),
    ]

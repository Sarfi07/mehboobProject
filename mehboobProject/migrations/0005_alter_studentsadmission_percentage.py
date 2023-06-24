# Generated by Django 4.1.7 on 2023-06-24 11:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehboobProject', '0004_rename_date_of_birth_studentsadmission_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsadmission',
            name='percentage',
            field=models.FloatField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(40)]),
        ),
    ]

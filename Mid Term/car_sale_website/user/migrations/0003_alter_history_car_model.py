# Generated by Django 5.0.1 on 2024-03-03 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_model', '0003_rename_brand_comment_car_model'),
        ('user', '0002_rename_brand_history_car_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_model.carmodel'),
        ),
    ]

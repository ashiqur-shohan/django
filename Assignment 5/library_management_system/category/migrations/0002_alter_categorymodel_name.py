# Generated by Django 5.0.1 on 2024-03-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-03 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='brand',
            new_name='car_model',
        ),
        migrations.RemoveField(
            model_name='history',
            name='car_price',
        ),
        migrations.RemoveField(
            model_name='history',
            name='car_qty',
        ),
        migrations.RemoveField(
            model_name='history',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='history',
            name='image',
        ),
        migrations.RemoveField(
            model_name='history',
            name='name',
        ),
    ]

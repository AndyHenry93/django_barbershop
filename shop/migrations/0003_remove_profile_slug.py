# Generated by Django 4.2 on 2023-04-07 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='slug',
        ),
    ]
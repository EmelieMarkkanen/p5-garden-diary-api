# Generated by Django 3.2.19 on 2023-06-02 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
    ]

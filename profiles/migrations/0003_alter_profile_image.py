# Generated by Django 3.2.19 on 2023-06-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_image', upload_to='images/'),
        ),
    ]

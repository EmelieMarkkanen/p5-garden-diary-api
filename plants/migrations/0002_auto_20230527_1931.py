# Generated by Django 3.2.19 on 2023-05-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plants',
            name='perennial',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
        migrations.AddField(
            model_name='plants',
            name='planted',
            field=models.DateField(blank=True, null=True),
        ),
    ]

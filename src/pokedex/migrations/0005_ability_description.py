# Generated by Django 3.0.4 on 2020-03-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0004_auto_20200310_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='ability',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]

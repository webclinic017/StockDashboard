# Generated by Django 4.0 on 2022-01-21 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listItems', '0005_searchfield_is_duplicate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchfield',
            name='is_duplicate',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 5.1.7 on 2025-04-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edible', '0002_cutleryfactory_delete_edibleitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutleryfactory',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]

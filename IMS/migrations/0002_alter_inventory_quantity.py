# Generated by Django 4.2.5 on 2023-10-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]

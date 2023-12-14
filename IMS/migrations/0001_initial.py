# Generated by Django 4.2.5 on 2023-09-29 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('IIN', models.CharField(blank=True, max_length=10, null=True)),
                ('Cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('Quantity_sold', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('Selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Profit_earned', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('Revenue', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('Selling_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Transactiondttm', models.DateTimeField(blank=True, null=True)),
                ('Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IMS.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('Cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Orderdttm', models.DateTimeField(blank=True, null=True)),
                ('Is_received', models.BooleanField(default=False)),
                ('Is_cancel', models.BooleanField(default=False)),
                ('Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='IMS.inventory')),
            ],
        ),
    ]
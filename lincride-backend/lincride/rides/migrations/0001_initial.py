# Generated by Django 5.1.6 on 2025-02-15 10:32

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.DecimalField(decimal_places=8, max_digits=19)),
                ('traffic_level', models.CharField(choices=[('low', 'low,'), ('normal', 'normal'), ('high', 'high')], max_length=10)),
                ('demand_level', models.CharField(choices=[('normal', 'normal'), ('peak', 'peak')], max_length=10)),
                ('traffic_multipier', models.DecimalField(decimal_places=2, max_digits=19)),
                ('demand_multipier', models.DecimalField(decimal_places=2, max_digits=19)),
                ('time_multiplier', models.DecimalField(decimal_places=1, max_digits=3)),
                ('distance_fare', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=19)),
                ('total_fare', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=19)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rider_rides', to='rides.rider')),
            ],
        ),
    ]

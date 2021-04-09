# Generated by Django 3.1.7 on 2021-04-08 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_auto_20210313_1337'),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resta_name', models.CharField(max_length=50)),
                ('has_AC', models.BooleanField(default=False)),
                ('has_delivery', models.BooleanField(default=False)),
                ('has_Banquethalls', models.BooleanField(default=False)),
                ('has_parking', models.BooleanField(default=False)),
                ('resta_contact', models.IntegerField(max_length=10)),
                ('resta_address', models.CharField(max_length=150)),
                ('resta_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.serviceprovider')),
                ('resta_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.place')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.CharField(max_length=10)),
                ('food_cost', models.IntegerField(max_length=4)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant')),
            ],
        ),
    ]

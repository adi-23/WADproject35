# Generated by Django 3.1.6 on 2021-05-04 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0004_remove_serviceprovider_choice'),
        ('hotels', '0002_hotel_hotel_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoppingcomplex_name', models.CharField(max_length=50)),
                ('shoppingcomplex_address', models.CharField(max_length=100)),
                ('shoppingcomplex_hasFloors', models.CharField(max_length=2)),
                ('shoppingcomplex_contactinfo', models.CharField(max_length=10)),
                ('shoppingcomplex_image', models.ImageField(upload_to='pics/')),
                ('shoppingcomplex_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.place')),
                ('shoppingcomplex_sp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.serviceprovider')),
            ],
        ),
    ]

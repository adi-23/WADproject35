# Generated by Django 3.1.7 on 2021-04-16 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_auto_20210416_1549'),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_itemtype', models.CharField(choices=[('HN', 'HomeNeeds'), ('ELE', 'Electrial'), ('STN', 'Stationary'), ('CLTH', 'Clothing'), ('BNKM', 'Banking and Money'), ('FAN', 'Fashion and jewlery'), ('SPRT', 'Sport'), ('FUN', 'Furniture')], default='HN', max_length=20)),
                ('shop_name', models.CharField(max_length=25)),
                ('shop_address', models.CharField(max_length=100)),
                ('shop_contactinfo', models.CharField(max_length=10)),
                ('shop_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.serviceprovider')),
                ('shop_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.place')),
            ],
        ),
    ]

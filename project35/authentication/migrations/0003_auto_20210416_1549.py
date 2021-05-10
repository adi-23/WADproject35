# Generated by Django 3.1.7 on 2021-04-16 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210313_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='choice',
            field=models.CharField(choices=[('SH', 'Shops'), ('HS', 'Hostes'), ('RS', 'Restaurents'), ('HO', 'Hospitals'), ('SM', 'Shopping malls'), ('CH', 'Cinema halls'), ('TS', 'Tourism')], max_length=2),
        ),
    ]

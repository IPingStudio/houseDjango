# Generated by Django 3.1.1 on 2020-09-30 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
        ('lease', '0004_auto_20200926_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaseinfo',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='house.houseinfo'),
        ),
    ]

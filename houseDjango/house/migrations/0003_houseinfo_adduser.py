# Generated by Django 3.1.1 on 2020-10-20 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import house.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0002_auto_20201017_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinfo',
            name='addUser',
            field=models.ForeignKey(default=house.models.get_superUser, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]

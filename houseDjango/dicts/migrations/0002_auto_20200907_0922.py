# Generated by Django 3.1.1 on 2020-09-07 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dicttype',
            name='sign',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dict',
            name='label',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='dicttype',
            name='label',
            field=models.CharField(max_length=20),
        ),
    ]

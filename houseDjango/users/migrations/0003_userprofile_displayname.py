# Generated by Django 3.1.1 on 2020-09-26 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200925_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='displayName',
            field=models.CharField(default=1, max_length=150, verbose_name='显示名称'),
            preserve_default=False,
        ),
    ]

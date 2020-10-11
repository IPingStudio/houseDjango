# Generated by Django 3.1.1 on 2020-09-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0002_auto_20200926_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaseinfo',
            name='acceptID',
            field=models.CharField(blank=True, help_text='受理编号', max_length=20, null=True, verbose_name='受理编号'),
        ),
        migrations.AlterField(
            model_name='leaseinfo',
            name='arbitrationUnits',
            field=models.CharField(blank=True, help_text='仲裁单位', max_length=20, null=True, verbose_name='仲裁单位'),
        ),
        migrations.AlterField(
            model_name='leaseinfo',
            name='holderPhone',
            field=models.CharField(blank=True, help_text='承租人电话', max_length=20, null=True, verbose_name='承租人电话'),
        ),
        migrations.AlterField(
            model_name='leaseinfo',
            name='leasePayMoney',
            field=models.CharField(blank=True, help_text='缴款金额', max_length=20, null=True, verbose_name='缴款金额'),
        ),
        migrations.AlterField(
            model_name='leaseinfo',
            name='leaseStatus',
            field=models.IntegerField(blank=True, help_text='状态_Dict', null=True, verbose_name='状态'),
        ),
    ]
# Generated by Django 2.2a1 on 2019-06-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20190621_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.IntegerField(default=''),
        ),
    ]

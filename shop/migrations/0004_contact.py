# Generated by Django 2.2a1 on 2019-06-15 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190405_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('Email', models.CharField(default='', max_length=60)),
                ('phone', models.CharField(default='', max_length=20)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
    ]

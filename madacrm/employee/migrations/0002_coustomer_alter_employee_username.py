# Generated by Django 4.1.3 on 2022-11-07 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phonenumber', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('registerdate', models.DateTimeField(default=datetime.datetime(2022, 11, 8, 0, 24, 44, 498424))),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
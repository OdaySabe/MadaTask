# Generated by Django 4.1.3 on 2022-11-07 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_service_alter_coustomer_registerdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coustomer',
            name='registerdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 8, 0, 33, 56, 242102)),
        ),
    ]
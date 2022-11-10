# Generated by Django 4.1.3 on 2022-11-07 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_coustomer_alter_employee_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('discription', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='coustomer',
            name='registerdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 8, 0, 31, 58, 683217)),
        ),
        migrations.AddField(
            model_name='coustomer',
            name='services',
            field=models.ManyToManyField(null=True, to='employee.service'),
        ),
    ]
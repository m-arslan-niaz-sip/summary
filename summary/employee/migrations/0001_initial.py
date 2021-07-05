# Generated by Django 3.2.5 on 2021-07-05 11:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('timestemp', models.DateTimeField(default=datetime.datetime(2021, 7, 5, 16, 29, 11, 901903))),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('timestemp', models.DateTimeField(default=datetime.datetime(2021, 7, 5, 16, 29, 11, 902899))),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.department')),
            ],
        ),
    ]

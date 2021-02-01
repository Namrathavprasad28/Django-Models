# Generated by Django 3.1.3 on 2021-01-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('edesig', models.CharField(max_length=40)),
                ('edob', models.DateField()),
                ('eexp', models.FloatField()),
                ('esal', models.IntegerField()),
            ],
        ),
    ]

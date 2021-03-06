# Generated by Django 3.0.8 on 2020-07-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=64, verbose_name='Day of the week')),
                ('start_time', models.TimeField(verbose_name='Start')),
                ('end_time', models.TimeField(verbose_name='End')),
                ('subject', models.CharField(max_length=64, verbose_name='Subject Name')),
            ],
        ),
    ]

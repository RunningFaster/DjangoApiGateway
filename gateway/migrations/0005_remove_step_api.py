# Generated by Django 3.1.7 on 2021-06-05 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0004_step_sort'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='api',
        ),
    ]
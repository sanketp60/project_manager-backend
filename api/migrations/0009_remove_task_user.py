# Generated by Django 3.2.9 on 2021-11-17 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20211117_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='User',
        ),
    ]

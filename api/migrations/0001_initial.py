# Generated by Django 3.2.9 on 2021-11-15 13:47

from django.db import migrations, models
import django.utils.timezone
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ProjectID', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('ProjectName', models.CharField(max_length=100)),
                ('ProjectDescription', models.TextField()),
                ('ProjectDuration', models.CharField(max_length=5)),
                ('ProjectAvatar', models.ImageField(upload_to='avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('TaskID', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('TaskName', models.CharField(max_length=100)),
                ('TaskDescription', models.TextField()),
                ('TaskStartDate', models.DateField(default=django.utils.timezone.now)),
                ('TaskEndDate', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]

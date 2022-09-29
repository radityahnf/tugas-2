# Generated by Django 4.1 on 2022-09-29 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]

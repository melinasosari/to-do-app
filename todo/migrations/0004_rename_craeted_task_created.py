# Generated by Django 5.0.1 on 2024-01-24 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_options_alter_task_craeted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='craeted',
            new_name='created',
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_expire_date_task_craeted_task_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_done']},
        ),
        migrations.AlterField(
            model_name='task',
            name='craeted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

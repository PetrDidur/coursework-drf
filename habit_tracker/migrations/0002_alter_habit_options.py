# Generated by Django 5.0 on 2023-12-09 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
    ]

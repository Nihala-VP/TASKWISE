# Generated by Django 5.0.1 on 2025-07-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('in-progress', 'in-progress'), ('completed', 'completed')], default='pending', max_length=200),
        ),
    ]

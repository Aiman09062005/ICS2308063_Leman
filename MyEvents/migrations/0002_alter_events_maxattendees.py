# Generated by Django 5.1.3 on 2025-01-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyEvents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='maxattendees',
            field=models.CharField(max_length=4),
        ),
    ]

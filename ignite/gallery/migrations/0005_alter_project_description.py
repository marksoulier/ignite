# Generated by Django 4.2.3 on 2023-08-03 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_project_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='No description'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-22 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_project_contact_info_project_image2_project_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contact_info',
            field=models.CharField(blank=True, default='No contact info', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='related_links',
            field=models.CharField(blank=True, default='No related links', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='sub_category',
            field=models.CharField(blank=True, default='No sub category', max_length=200),
        ),
    ]

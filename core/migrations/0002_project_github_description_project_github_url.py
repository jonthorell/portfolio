# Generated by Django 5.0 on 2024-01-18 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_description',
            field=models.CharField(blank=True, default='Add description', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.CharField(default='localhost', max_length=60),
        ),
    ]

# Generated by Django 4.2 on 2024-02-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitelogic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='univarsty',
            name='price',
            field=models.CharField(default='000'),
        ),
    ]

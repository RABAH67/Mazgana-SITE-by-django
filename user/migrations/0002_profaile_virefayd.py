# Generated by Django 4.2 on 2024-02-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profaile',
            name='virefayd',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.2 on 2024-02-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Univarsty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='univarsty/')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('univarstyURL', models.URLField()),
            ],
        ),
    ]

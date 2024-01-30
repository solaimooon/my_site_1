# Generated by Django 5.0.1 on 2024-01-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.TimeField(auto_now=True)),
            ],
        ),
    ]

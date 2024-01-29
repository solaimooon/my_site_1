# Generated by Django 5.0.1 on 2024-01-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='detail',
            new_name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='counted_view',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

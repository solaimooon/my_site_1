# Generated by Django 5.0.1 on 2024-02-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='image/defualt.jpg', upload_to='image/'),
        ),
    ]

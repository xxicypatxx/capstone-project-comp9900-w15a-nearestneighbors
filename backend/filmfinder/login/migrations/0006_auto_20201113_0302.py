# Generated by Django 3.1.2 on 2020-11-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20201108_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='../movies/user_dp/default.png', upload_to='../movies/user_dp'),
        ),
    ]
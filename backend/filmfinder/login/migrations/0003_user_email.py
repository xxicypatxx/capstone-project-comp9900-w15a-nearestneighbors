# Generated by Django 3.1.2 on 2020-10-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20201029_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='N/A', max_length=50),
        ),
    ]

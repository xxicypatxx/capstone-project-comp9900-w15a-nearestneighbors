# Generated by Django 3.1.2 on 2020-10-29 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['uid'], 'verbose_name': 'user'},
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-05 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20201103_0324'),
        ('movies', '0015_user_banned_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_banned_list',
            name='banned_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_banned_this_user_set', to='login.user'),
        ),
        migrations.AlterField(
            model_name='user_banned_list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned_user_set', to='login.user'),
        ),
    ]

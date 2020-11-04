# Generated by Django 3.1.2 on 2020-11-04 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'cast',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('region', models.TextField(blank=True, null=True)),
                ('released_date', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie_genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MoviePosters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Movie_Posters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_comment', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('votecount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('profile_photo', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserBannedList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banned_user_id', models.IntegerField(blank=True, db_column='banned_user_ID', null=True)),
            ],
            options={
                'db_table': 'user_banned_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WatchHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_date', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'watch_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'wish_list',
                'managed': False,
            },
        ),
    ]

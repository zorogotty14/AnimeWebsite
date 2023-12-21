# Generated by Django 4.2.6 on 2023-11-13 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('aired', models.TextField()),
                ('studios', models.TextField(max_length=200)),
                ('type', models.CharField(default='series', max_length=200)),
                ('description', models.TextField()),
                ('img', models.TextField()),
                ('video', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AnimeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default=0)),
                ('name', models.TextField(default=0)),
                ('aired', models.TextField(default=0)),
                ('studios', models.TextField(default=0, max_length=200)),
                ('type', models.CharField(default='series', max_length=200)),
                ('description', models.TextField(default=0)),
                ('img', models.TextField(default=0)),
                ('video', models.TextField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
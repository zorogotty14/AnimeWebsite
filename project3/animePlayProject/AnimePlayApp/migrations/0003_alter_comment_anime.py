# Generated by Django 4.2.6 on 2023-11-17 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AnimePlayApp', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimePlayApp.anime'),
        ),
    ]

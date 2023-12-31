# Generated by Django 4.2.5 on 2023-09-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_actor_alter_movie_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actor',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies_acted', to='movie.actor'),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_game_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='trials',
            field=models.IntegerField(null=True),
        ),
    ]

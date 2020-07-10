from django.db import models


class Player(models.Model):
    player_id = models.CharField(max_length=200)

    def __str__(self):
        return self.player_id


class Game(models.Model):
    game_id = models.CharField(max_length=200)
    number = models.IntegerField(null=True)
    is_finished = models.BooleanField(default=False)
    trials = models.IntegerField(default=0)
    players = models.ManyToManyField(
        Player,
        through='PlayerGameInfo',
        through_fields=('game', 'player'),
    )


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    is_owner = models.BooleanField(null=True)

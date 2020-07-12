from django.db import models


class Player(models.Model):
    player_id = models.CharField(max_length=200,
                                 verbose_name='Игрок', )        # Записываем session_id игрока

    def __str__(self):
        return self.player_id


class Game(models.Model):
    # Записываем session_id игрока, который создал игру
    game_id = models.CharField(max_length=200,
                               verbose_name='Игра', )

    # Число, которое загодал игрок
    number = models.IntegerField(null=True,
                                 verbose_name='Загаданное число', )

    # Если число отгадано хотя бы один раз, то игра завершается
    is_finished = models.BooleanField(default=False,
                                      verbose_name='Признак окончания игры', )

    # Количетсво попыток, которое потрачено на отгадывание
    trials = models.IntegerField(default=0,
                                 verbose_name='Количество попыток', )

    # Основатель и игроки, которые пытались отгадать
    players = models.ManyToManyField(
        Player,
        through='PlayerGameInfo',
        through_fields=('game', 'player'),
    )


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    # Признак создателя игры
    is_owner = models.BooleanField(null=True,
                                   verbose_name='Основатель игры', )

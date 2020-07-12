from django.shortcuts import render, redirect

from game.forms import NewGame, GamePlay
from game.models import Player, Game, PlayerGameInfo


def get_session_id(request):
    try:
        return request.COOKIES['sessionid']
    except KeyError:
        return 'anonymous'


def show_home(request):
    # Стартовая страница

    return render(request, 'home.html', {'session_id': get_session_id(request), }, )


def new_game(request, session_id):
    form = NewGame()

    # Форма по созданию игры
    if request.method == 'POST':
        form = NewGame(request.POST)
        if form.is_valid() and form['number'].value():
            if not Player.objects.filter(player_id=session_id):
                Player(player_id=session_id).save()
            Game(game_id=session_id, number=form['number'].value()).save()
            PlayerGameInfo(player_id=Player.objects.filter(player_id=session_id).values('id')[0]['id'],
                           game_id=Game.objects.order_by('-id').filter(game_id=session_id).values('id')[0]['id'],
                           is_owner=True).save()
            return redirect('game_created',
                            game_id=Game.objects.order_by('-id').filter(game_id=session_id).values('id')[0]['id'])

    return render(request, 'new_game.html', {'form': form, }, )


def game_created(request, game_id):

    # Уведомление о создании игры
    return render(request, 'game_created.html',
                  {'number': Game.objects.filter(id=game_id).values('number')[0]['number'], }, )


def games_list(request):

    # Вывод списка активных игр, отображаются игры, которые созданы другим пользователем
    try:
        games = Game.objects.filter(is_finished=False).exclude(players__player_id=get_session_id(request)).values('id', 'game_id')
    except IndexError:
        games = []

    return render(request,
                  'games_list.html',
                  {'games': games, }, )


def games_finished(request):

    # Вывод списка всех завершенных игр
    try:
        games = Game.objects.filter(is_finished=True).values('id', 'game_id')
    except IndexError:
        games = []

    return render(request,
                  'games_finished.html',
                  {'games': games, }, )


def game_finished(request, game_id):

    # Вывод завершенной игры
    try:
        games = Game.objects.filter(id=game_id).values('game_id', 'number', 'trials', )
    except IndexError:
        games = []

    return render(request,
                  'game_finished.html',
                  {'games': games[0], }, )


def game(request, game_id):
    form = GamePlay()
    session_id = get_session_id(request)

    # Получение данных с формы
    if request.method == 'POST':
        form = GamePlay(request.POST)
        if form.is_valid() and form['guess'].value():
            if not Player.objects.filter(player_id=session_id):
                Player(player_id=session_id).save()
            # Game(game_id=session_id, number=form['number'].value()).save()
            if not (PlayerGameInfo.objects.filter(
                    player_id=Player.objects.filter(player_id=session_id).values('id')[0]['id']).values('game_id')[0][
                        'game_id'] == game_id):
                PlayerGameInfo(player_id=Player.objects.filter(player_id=session_id).values('id')[0]['id'],
                               game_id=game_id,
                               is_owner=False).save()

            # Учет количества попыток
            if not Game.objects.filter(id=game_id).values('is_finished')[0]['is_finished']:
                set_trials = Game.objects.get(id=game_id)
                set_trials.trials += 1
                set_trials.save()

            # Проверка выигрыша и обновление формы
            if int(form['guess'].value()) == Game.objects.filter(id=game_id).values('number')[0]['number']:
                guess = 'Вы угадали число!'
                set_finished = Game.objects.get(id=game_id)
                set_finished.is_finished = True
                set_finished.save()
            else:
                if int(form['guess'].value()) > Game.objects.filter(id=game_id).values('number')[0]['number']:
                    guess = f"Заданное число меньше {form['guess'].value()}"
                else:
                    guess = f"Заданное число больше {form['guess'].value()}"
            form = GamePlay()
            return render(request, 'game.html', {'form': form, 'guess': guess, })

    return render(request, 'game.html', {'form': form, })

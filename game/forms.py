from django import forms


class NewGame(forms.Form):
    number = forms.IntegerField(label='Загадай число')


class GamePlay(forms.Form):
    guess = forms.IntegerField(label='Отгадай число')


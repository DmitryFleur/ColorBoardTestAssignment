from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import NumberInput, Textarea


class GameSettingsForm(forms.Form):
    number_of_players = forms.IntegerField(
        label='The​ ​number​ ​of​ ​players',
        initial=2,
        validators=[MinValueValidator(1),
                    MaxValueValidator(4)],
        widget=NumberInput(attrs={'class': 'form-control'}))
    squares_on_board = forms.IntegerField(
        label='The​ ​number​ ​of​ ​squares​ ​on​ ​the​ ​board​',
        initial=13,
        validators=[MinValueValidator(1),
                    MaxValueValidator(79)],
        widget=NumberInput(attrs={'class': 'form-control'}))
    number_cards_in_the_deck = forms.IntegerField(
        label='The​ ​number​ ​of​ ​cards​ ​in​ ​the​ ​deck',
        initial=8,
        validators=[MinValueValidator(1),
                    MaxValueValidator(200)],
        widget=NumberInput(attrs={'class': 'form-control'}))
    characters_on_board = forms.CharField(
        label='The​ ​characters​ ​representing​ ​the​ ​colored​ ​squares​ ​on​ ​the​ ​board',
        widget=Textarea(attrs={'class': 'form-control', 'rows': 2}))
    cards_in_the_deck = forms.CharField(
        label='The​ ​cards​ ​in​ ​the​ ​deck​',
        widget=Textarea(attrs={'class': 'form-control', 'rows': 2}))

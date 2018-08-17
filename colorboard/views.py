from django.shortcuts import render
from django.views import View
from .forms import GameSettingsForm
from .game import Game
from .models import GameResults


class ColorBoardView(View):
    def get(self, request):
        form = GameSettingsForm()
        result = None
        return render(request, 'forms/game_settings.html', {'form': form, 'result': result})

    def post(self, request):
        form = GameSettingsForm(request.POST)
        result = None
        if form.is_valid():
            data = form.cleaned_data
            number_of_players = data['number_of_players']
            squares_on_board = data['squares_on_board']
            number_cards_in_the_deck = data['number_cards_in_the_deck']
            characters_on_board = data['characters_on_board']
            cards_in_the_deck = data['cards_in_the_deck']
            game = Game(number_of_players,
                        squares_on_board,
                        number_cards_in_the_deck,
                        characters_on_board,
                        cards_in_the_deck)
            result = game.run_game()

            GameResults(number_of_players, squares_on_board, number_cards_in_the_deck,
                        characters_on_board, cards_in_the_deck, result).save()

        return render(request, 'forms/game_settings.html', {'form': form, 'result': result})


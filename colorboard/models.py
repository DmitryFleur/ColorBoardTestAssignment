from django.db import models


class GameResults(models.Model):
    number_of_players = models.IntegerField()
    squares_on_board = models.IntegerField()
    number_cards_in_the_deck = models.IntegerField()
    characters_on_board = models.CharField(max_length=200)
    cards_in_the_deck = models.CharField(max_length=400)
    result = models.CharField(max_length=50)

class Game(object):
    def __init__(self, number_of_players, squares_on_board, number_cards_in_the_deck,
                 characters_on_board, cards_in_the_deck):
        self.number_of_players = number_of_players
        self.squares_on_board = squares_on_board
        self.number_cards_in_the_deck = number_cards_in_the_deck
        self.characters_on_board = characters_on_board.upper()
        self.cards_in_the_deck = cards_in_the_deck.upper()

    @staticmethod
    def players_cards(player, cards):
        player_index = 0
        card_index = 0

        while card_index < len(cards):
            if player_index >= len(player):
                player_index = 0
            yield (card_index, player[player_index], cards[card_index])
            player_index += 1
            card_index += 1

    def run_game(self):
        cards = self.cards_in_the_deck.split(',')
        players = range(1, self.number_of_players + 1)
        player_position = dict((x, -1) for x in players)

        if len(cards) != self.number_cards_in_the_deck:
            return 'Wrong number of cards in the deck.'

        for index, player, cards in self.players_cards(players, cards):
            for card in cards:
                print(cards, card, index)
                position = player_position[player]
                found = self.characters_on_board.find(card, position + 1)
                if found < 0 or found == self.squares_on_board:
                    return 'Player %s won after %s cards.' % (player, index + 1)
                player_position[player] = found

        return 'No player won after %s cards.' % self.number_cards_in_the_deck

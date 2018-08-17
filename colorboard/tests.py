import unittest
from .game import Game


class TestGameResults(unittest.TestCase):
    def testResults(self):
        data = [[2, 13, 8, '​RYGPBRYGBRPOP', 'R,B,GG,Y,P,B,P,RR', 'Player 1 won after 7 cards.'],
                [2, 6, 5, 'RYGRYB', 'R,YY,G,G,B', 'Player 2 won after 4 cards.'],
                [3, 9, 6, 'QQQQQQQQQ', 'Q,QQ,Q,Q,QQ,Q', 'No player won after 6 cards.']]

        for case in data:
            game = Game(case[0], case[1], case[2], case[3], case[4])
            result = game.run_game()
            self.assertEquals(result, case[5])
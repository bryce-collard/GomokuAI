import math


class Metrics:

    def __init__(self):
        self.black_wins = 0 #min
        self.white_wins = 0 #max
        self.count = 0

    def update(self, score):
        if score > 0:
            self.white_wins += 1
        elif score < 0:
            self.black_wins += 1
        self.count += 1

    def get_p_win(self, player):
        try:
            if player == 'B':
                return self.black_wins / self.count
            elif player == 'W':
                return self.white_wins / self.count
            else:
                raise ValueError('player {} must be W or B'.format(player))
        except ZeroDivisionError:
            raise ValueError('must be updated at least once \
                              to get win probability')

    def get_expected_value(self, player):
        try:
            if player == 'B':
                return (self.black_wins - self.white_wins) / self.count
            elif player == 'W':
                return (self.white_wins - self.black_wins) / self.count
            else:
                raise ValueError('player {} must be B or W'.format(player))
        except ZeroDivisionError:
            raise ValueError('must be updated at least once \
                              to get expected value')

    def get_explore_term(self, parent, c=1.41):
        if parent.count:
            return c * (math.log(parent.count) / self.count) ** (1 / 2)
        else:
            return 0

    def get_ucb(self, player, parent, c=1.41, default=6):
        if self.count:
            p_win = self.get_p_win(player)
            explore_term = self.get_explore_term(parent)
            return p_win + explore_term
        else:
            return default

from learning import *
from production import *

import itertools
import math

class Farmer:
    def __init__(self, river, position):
        self.river = river
        self.position = position
        self.investment = 0
        self.endowment = 0

        self.strategies = self.available_strategies()
        self.learning = Learning(n = len(self.strategies))

    def possible_investments(self):
        return range(4)

    def available_strategies(self):
        return list(itertools.product(self.possible_investments(),
                    [Production(0, 2, 2, 1),
                     Production(0, 1, 1, 1),
                     Production(2, 1, 1, 3),
                     Production(2, 1, 0, 4),
                     Production(3, 2, 0, 6)]))

    def action_space(self, ll, ul):
        return range(ll, ul + 1)

    def profit(self, water):
        return math.sqrt(water)

    def choice(self):
        chosen = self.strategies[self.learning.choose()]

        self.endowment -= chosen[0]
        self.endowment -= chosen[1].input_money

        return chosen

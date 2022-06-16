from learning import *
from production import *

import itertools
import math

class Farmer:
    def __init__(self, river, position, learn_params = (0.1, 3, None)):   
        self.river = river
        self.position = position
        self.investment = 0
        self.endowment = 0

        self.initial = (river, position, self.investment, self.endowment)

        self.strategies = self.available_strategies()
        self.learn = ReinforcementSimple(alpha = learn_params[0],
                                         lambda_ = learn_params[1],
                                         n = len(self.strategies),
                                         seed = learn_params[2])

    def possible_investments(self):
        return range(4)

    def available_strategies(self):
        return list(itertools.product(self.possible_investments(),
                    [Production(0, 2, 2, 1),
                     Production(0, 1, 1, 1),
                     Production(2, 1, 1, 3),
                     Production(2, 1, 0, 4),
                     Production(3, 2, 0, 6)]))

    def reset(self):
        self.river = self.initial[0]
        self.position = self.initial[1]
        self.investment = self.initial[2]
        self.endowment = self.initial[3]
    
    def choice(self):
        chosen = self.strategies[self.learn.choose()]

        self.endowment -= chosen[0] # investment cannot be recovered
        self.endowment -= chosen[1].input_money

        return chosen

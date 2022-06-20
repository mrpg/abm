import itertools
import math

from production import Production


class Farmer:
    def __init__(self, river, learn_model, learn_args=None):
        self.river = river
        self.investment = 0
        self.endowment = 0

        self.initial = (river, self.investment, self.endowment)

        self.strategies = self.available_strategies()
        self.learn = learn_model(n=len(self.strategies), **learn_args)

    def possible_investments(self):
        return range(4)

    def available_strategies(self):
        return list(
            itertools.product(
                self.possible_investments(),
                [
                    Production("A1", 0, 2, 2, 1),
                    Production("A2", 0, 1, 1, 1),
                    Production("A3", 2, 1, 1, 3),
                    Production("A4", 2, 1, 0, 4),
                    Production("A5", 3, 2, 0, 6),
                ],
            )
        )

    def reset(self):
        self.river = self.initial[0]
        self.investment = self.initial[1]
        self.endowment = self.initial[2]

    def choice(self):
        chosen = self.strategies[self.learn.choose()]

        self.endowment -= chosen[0]  # investment cannot be recovered
        self.endowment -= chosen[1].input_money

        return chosen

import random

import numpy as np

class Learning:
    # random "learning", also general-purpose super-class
    def __init__(self, **kwargs):
        self.parameters = kwargs
        self.history = []

    def __getitem__(self, name):
        return self.parameters[name]

    def __setitem__(self, name, value):
        self.parameters[name] = value

    def choose(self):
        return random.choice(range(self['n']))

    def update(self, action, reward):
        pass

    def archive(self, **kwargs):
        self.history.append(kwargs)

class ReinforcementSimple(Learning):
    def __init__(self, alpha, lambda_, n, seed = None, values = None):
        super().__init__(alpha = alpha, lambda_ = lambda_, n = n)
        self.rng = np.random.default_rng(seed)

        if values is None:
            self.values = np.ones(n)
        else:
            self.values = values

    def transformed_values(self):
        return np.exp(self['lambda_']*self.values)

    def probabilities(self):
        return self.transformed_values()/sum(self.transformed_values())

    def choose(self):
        return self.rng.choice(self['n'], p = self.probabilities())

    def update(self, action, reward):
        self.values[action] = (1-self['alpha'])*self.values[action] + self['alpha']*reward

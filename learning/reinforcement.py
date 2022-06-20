import numpy as np

from . import Learning


class Reinforcement(Learning):
    def __init__(self, alpha, lambda_, n, rng=None, values=None):
        super().__init__(alpha=alpha, lambda_=lambda_, n=n)

        if rng is None:
            self.rng = np.random.default_rng()
        else:
            self.rng = rng

        if values is None:
            self.values = np.zeros(n)
        else:
            self.values = values

    def transformed_values(self):
        return np.exp(self["lambda_"] * self.values)

    def probabilities(self):
        return self.transformed_values() / sum(self.transformed_values())

    def choose(self):
        return self.rng.choice(self["n"], p=self.probabilities())

    def update(self, action, reward):
        # print(f'{action} -> {reward}, value: {self.values[action]}', end = '')
        self.values[action] = (1 - self["alpha"]) * self.values[action] + self["alpha"] * reward
        # print(f' -> {self.values[action]}')

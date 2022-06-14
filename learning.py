import random

class Learning:
    def __init__(self, n):
        self.n = n

    def choose(self):
        # TODO: is just random at the moment
        return random.choice(range(self.n))

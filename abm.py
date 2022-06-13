import math

class Farmer:
    def __init__(self, river, position, alpha):
        self.river = river
        self.position = position
        self.alpha = alpha

    def other_regarding(self):
        return 0

    def profit(self, water):
        return water

    def extraction(self, action_space):
        x_opt = 0
        y_opt = -1e9

        for action in action_space:
            if self.profit(action) > y_opt:
                y_opt = self.utility(action)
                x_opt = action

        return x_opt

    def utility(self, water):
        return self.alpha*self.profit(water) + (1-self.alpha)*self.other_regarding()

class River:
    def __init__(self, rate):
        self.rate = rate
        self.farmers = []

    def add_farmer(self, alpha):
        next_pos = len(self.farmers)
        new_farmer = Farmer(self, next_pos, alpha)

        self.farmers.append(new_farmer)

    def get_farmers(self):
        return self.farmers

    def one_run(self):
        amount = self.rate
        extractions = []

        for farmer in self.farmers:
            this_one = farmer.extraction(range(0, amount + 1))
            extractions.append(this_one)
            amount = amount - this_one

        return extractions

if __name__ == '__main__':
    r = River(10)

    for _ in range(4):
        r.add_farmer(1)

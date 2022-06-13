from farmer import *

class River:
    def __init__(self, rate):
        self.rate = rate
        self.farmers = []
        self.history = []

    def add_farmer(self, alpha):
        next_pos = len(self.farmers)
        new_farmer = Farmer(self, next_pos, alpha)

        self.farmers.append(new_farmer)

    def get_farmers(self):
        return self.farmers

    def outcomes(self, extractions):
        profits = sum(f.profit(e) for f, e in zip(self.farmers, extractions))
        outflow = self.rate - sum(extractions)

        return [profits, outflow]

    def another_run(self):
        amount = self.rate
        extractions = []

        for farmer in self.farmers:
            this_one = farmer.extraction(range(0, amount + 1))
            extractions.append(this_one)
            amount -= this_one

        self.history.append([extractions, self.farmers])

        return extractions

    def many_runs(self, n = 1000):
        all_extractions = []
        
        for _ in range(n):
            all_extractions.append(self.another_run())

        return all_extractions

from farmer import *

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
            amount -= this_one

        return extractions

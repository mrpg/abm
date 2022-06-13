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

    def welfare(self, extractions):
        profits = sum(f.profit(e) for f, e in zip(self.farmers, extractions))
        outflow = self.rate - sum(extractions)

        return [profits, outflow]

    def social_planner(self, welfare_index = 0):
        # hack: naive, inefficient and extremely limited
        # needs more RECURSION
        
        if len(self.farmers) != 4:
            raise ValueError('This function is currently only able to optimize for 4 agents')
            
        opt_x = None
        opt_y = float('-inf')
        ul = self.rate
        
        for i in self.farmers[0].action_space(0, ul):
            for j in self.farmers[1].action_space(0, ul-i):
                for k in self.farmers[2].action_space(0, ul-i-j):
                    for l in self.farmers[3].action_space(0, ul-i-j-k):
                        if (cur_y := self.welfare([i, j, k, l])[welfare_index]) > opt_y:
                            opt_x = [i, j, k, l]
                            opt_y = cur_y

        return opt_x

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

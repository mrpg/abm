from farmer import *

class River:
    def __init__(self, initial):
        self.amount = initial
        self.farmers = []

    def add_farmer(self, alpha):
        next_pos = len(self.farmers)
        new_farmer = Farmer(self, next_pos)

        self.farmers.append(new_farmer)

    def get_farmers(self):
        return self.farmers

    def groundwater(self):
        total_investment = sum(f.investment for f in self.farmers)

        return max(0, min(12, 2*total_investment - 4))

    def welfare(self):
        profits = sum(f.endowment for f in self.farmers)
        outflow = self.amount

        return [profits, outflow]

    def choice_feasible(self, choice):
        return self.amount >= choice.input_water

    def another_run(self):
        choices = [farmer.choice() for farmer in self.farmers]

        for farmer, choice in zip(self.farmers, choices):
            farmer.investment = choice[0]

        self.amount += self.groundwater()
        
        for farmer, choice in zip(self.farmers, choices):
            if self.choice_feasible(choice[1]):
                self.amount -= choice[1].input_water
                self.amount += choice[1].output_water
                farmer.endowment += choice[1].output_money

        # TODO: reset

        return {'choices': choices, 'welfare': self.welfare()} # TODO: to be defined, add individual profits

    def many_runs(self, n = 1000):
        all_runs = []
        
        for _ in range(n):
            all_runs.append(self.another_run())

        return all_runs

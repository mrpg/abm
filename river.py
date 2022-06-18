from farmer import *


class River:
    def __init__(self, initial):
        self.amount = initial
        self.initial = initial
        self.farmers = []

    def add_farmer(self, **kwargs):
        new_farmer = Farmer(self, **kwargs)

        self.farmers.append(new_farmer)

    def get_farmers(self):
        return self.farmers

    def groundwater(self):
        total_investment = sum(f.investment for f in self.farmers)

        return max(0, min(12, 2 * total_investment - 4))

    def welfare(self):
        profits = sum(f.endowment for f in self.farmers)
        outflow = self.amount

        return [profits, outflow]

    def choice_feasible(self, choice):
        return self.amount >= choice.input_water

    def reset(self):
        for farmer in self.farmers:
            farmer.reset()

        self.amount = self.initial

    def another_round(self, stochastic_inflow=None):
        self.reset()

        if stochastic_inflow is not None:
            self.amount = stochastic_inflow()

        choices = [farmer.choice() for farmer in self.farmers]

        for farmer, choice in zip(self.farmers, choices):
            farmer.investment = choice[0]

        self.amount += self.groundwater()

        for farmer, choice in zip(self.farmers, choices):
            if self.choice_feasible(choice[1]):
                self.amount -= choice[1].input_water
                self.amount += choice[1].output_water
                farmer.endowment += choice[1].output_money

            outcomes = {
                "choices": choices,
                "welfare": self.welfare(),
            }  # TODO: to be defined, add individual profits

        # after everything has happened, learn:
        for farmer, choice in zip(self.farmers, choices):
            farmer.learn.update(
                action=farmer.strategies.index(choice), reward=farmer.endowment
            )

            farmer.learn.archive(
                endowment=farmer.endowment,
                choice=choice,
                choice_id=farmer.strategies.index(choice),
                new_probs=farmer.learn.probabilities(),
            )

        return outcomes

    def many_rounds(self, n=10000, stochastic_inflow=None):
        all_rounds = []

        for _ in range(n):
            all_rounds.append(self.another_round(stochastic_inflow))

        return all_rounds

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

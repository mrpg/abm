import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__))) # hack (https://stackoverflow.com/a/49375740)

from learning import *

actions = [x for x in range(0, 12+1)]

def profit(a):
    x = actions[a]
    if x <= 5:
        return 2*(x-0)/((12)*(5))
    else:
        return 2*(12-x)/((12)*(12-5))

learner = ReinforcementSimple(0.1, 20, len(actions))

for _ in range(500):
    action = learner.choose()
    reward = profit(action)

    learner.update(action = action, reward = reward)
    learner.archive(pi = reward, p = learner.probabilities())

import matplotlib
import matplotlib.pyplot as plt

def plot(what = 'pi'):
    plt.plot(range(len(learner.history)), [h[what] for h in learner.history])

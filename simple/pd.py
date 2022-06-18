import os
import sys

sys.path.insert(
    1, os.path.join(sys.path[0], "..")
)  # hack: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder#comment23054549_11158224

from learning import *

COOP = 0
DEFECT = 1

actions = (COOP, DEFECT)


def profits(a1=COOP, a2=COOP):
    if a1 == COOP and a2 == COOP:
        return (3, 3)
    elif a1 == COOP and a2 == DEFECT:
        return (0, 5)
    elif a1 == DEFECT and a2 == COOP:
        return (5, 0)
    elif a1 == DEFECT and a2 == DEFECT:
        return (2, 2)
    else:
        raise ValueError


learners = [
    ReinforcementSimple(0.1, 1, len(actions)),
    ReinforcementSimple(0.1, 1, len(actions)),
]

for _ in range(500):
    actions = [l.choose() for l in learners]

    rewards = profits(*actions)

    for l, a, pi in zip(learners, actions, rewards):
        l.update(action=a, reward=pi)
        l.archive(pi=pi, p_coop=l.probabilities()[0])

import matplotlib
import matplotlib.pyplot as plt


def plot(whom=0, what="p_coop"):
    plt.plot(
        range(len(learners[whom].history)), [h[what] for h in learners[whom].history]
    )
